"""Check local profile links and passive SVG assets without network requests."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "img":
            if not attrs.get("alt", "").strip():
                raise ValueError("An image is missing alternative text")
            self.targets.append(attrs["src"])
        if tag == "source":
            self.targets.append(attrs["srcset"])


def check_target(source, target):
    url = urlsplit(target)
    if url.scheme or url.netloc or not url.path:
        return
    resolved = (source.parent / unquote(url.path)).resolve()
    if not resolved.is_relative_to(ROOT) or not resolved.exists():
        raise ValueError(f"Invalid local target in {source.name}: {target}")


def main():
    for name in ("README.md", "README.pt-BR.md", "docs/MAINTENANCE.md"):
        source = ROOT / name
        text = source.read_text(encoding="utf-8")
        parser = Images()
        parser.feed(text)
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in parser.targets + re.findall(r"\]\(([^\s)]+)\)", text):
            check_target(source, target)

    for asset in (ROOT / "assets").glob("*.svg"):
        tree = ET.parse(asset)
        root = tree.getroot()
        ns = {"svg": "http://www.w3.org/2000/svg"}
        if root.find("svg:title", ns) is None or root.find("svg:desc", ns) is None:
            raise ValueError(f"Missing SVG description: {asset.name}")
        for node in root.iter():
            tag = node.tag.rsplit("}", 1)[-1]
            if tag in {"script", "foreignObject", "image", "use", "style", "animate"}:
                raise ValueError(f"Unexpected active or external SVG element: {asset.name}")
            for key in node.attrib:
                if key.lower().startswith("on") or key.rsplit("}", 1)[-1] == "href":
                    raise ValueError(f"Unexpected SVG reference: {asset.name}")
    print("Profile links, image descriptions and passive SVG structure: OK")


if __name__ == "__main__":
    main()
