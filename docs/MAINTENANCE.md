# Maintaining this profile

Keep the English and [Portuguese](../README.pt-BR.md) READMEs in sync. Add a
technology only when a linked project demonstrates its use. Prefer working
examples and repository links to statistics or claims about experience.

When a project changes:

1. Run its tests and confirm the documented commands still work.
2. Update its short description, scope and example links in both profile READMEs.
3. Keep the strongest Python tools first. Keep web study projects in their own section.
4. Use the repository's live Actions page for CI status; avoid hard-coded test counts.
5. Run `python scripts/check_profile.py` before opening a pull request.

## Visual assets

The editable sources are SVG files in [assets](../assets). They use system fonts,
no third-party logos, scripts, embedded images, remote fonts or animation.
`banner-dark.svg` and `banner-light.svg`, plus their compact mobile variants,
are selected by a `picture` element;
the light banner is the fallback. Keep the alternative text descriptive.

| Role | Dark | Light |
| --- | --- | --- |
| Background | `#11191D` | `#F4F6F2` |
| Main text | `#F2F5F3` | `#15221E` |
| Secondary text | `#AABCB8` | `#4B6258` |
| Accent | `#D4FF63` | `#426600` |

The LC mark and short double rail are the shared graphic signature. Project covers
use the same spacing and colors, with different motifs for links and categories.
Detailed text lives in Markdown so the profile remains useful if images do not load.

The existing robot avatar remains the primary recommendation. `monogram.svg` and
`avatar-monogram.png` are optional alternatives; adding them here does not change
the account avatar.

## Optional PNG exports

SVGs are the editable sources. If a PNG needs to be refreshed, install CairoSVG in a
temporary development environment and run, for example:

```bash
python -m pip install cairosvg
python -m cairosvg assets/monogram.svg -o assets/avatar-monogram.png
```

Project social previews use `assets/social-preview.svg`, exported to a 1280 × 640
PNG. Upload the PNG through the repository's Settings → General → Social preview.
The file in the repository alone does not configure that setting.

Account bio, pinned repositories, social previews and security settings are managed
through GitHub's settings separately from these files. Review monthly dependency
update pull requests; merge only after the relevant checks pass.
