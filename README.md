<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/identity/profile-octocat.webp">
  <source media="(prefers-color-scheme: light)" srcset="./assets/identity/profile-light-premium.webp">
  <img src="./assets/identity/profile-octocat.webp" alt="Luiz Chockt — software development, Python and automation." width="1200">
</picture>

**Language:** English · [Português (Brasil)](./README.pt-BR.md)

[Projects](#selected-projects) · [Repositories](https://github.com/LuizChockt?tab=repositories)

# Hi, I'm Luiz.

I build **Python tools for Markdown, file organization and automation**, alongside web projects with **JavaScript, HTML and CSS**.

I'm a Systems Analysis and Development graduate based in Brazil. My background in law gives me a practical source of problems to solve with software: documents, information and repetitive work.

## Selected projects

### [ClipInbox](https://github.com/LuizChockt/clipinbox)

<img src="https://raw.githubusercontent.com/LuizChockt/clipinbox/main/assets/identity/cover-premium.webp" alt="ClipInbox — clipboard capture to Markdown" width="780">

I built ClipInbox to save clipboard text to a local Markdown inbox using a global Windows shortcut. It also lets users write quick notes from the system tray without opening Obsidian.

**Python · Tkinter · Win32 · pytest · GitHub Actions**

[Windows download](https://github.com/LuizChockt/clipinbox/releases/tag/v0.1.0) · [CI](https://github.com/LuizChockt/clipinbox/actions/workflows/ci-release.yml)

### [Markdown Link Auditor](https://github.com/LuizChockt/markdown-link-auditor)

<img src="https://raw.githubusercontent.com/LuizChockt/markdown-link-auditor/main/assets/identity/cover-premium.webp" alt="Markdown Link Auditor — audit local Markdown links and attachments" width="780">

I developed Markdown Link Auditor to find broken local references, missing attachments, ambiguous links and potential orphan notes in Markdown knowledge bases. It supports CommonMark and Obsidian wikilinks and generates deterministic text and JSON reports.

**Python · markdown-it-py · pytest · GitHub Actions**

The scanner reads files without modifying them, resolves Unicode paths and respects explicit filesystem boundaries. It counts external URLs without making HTTP requests.

[Code & quick start](https://github.com/LuizChockt/markdown-link-auditor#quick-start) · [Sample report](https://github.com/LuizChockt/markdown-link-auditor/blob/main/examples/reports/sample-report.txt) · [CI](https://github.com/LuizChockt/markdown-link-auditor/actions/workflows/tests.yml)

### [Legal Markdown Organizer](https://github.com/LuizChockt/legal-markdown-organizer)

<img src="https://raw.githubusercontent.com/LuizChockt/legal-markdown-organizer/main/assets/identity/cover-premium.webp" alt="Legal Markdown Organizer — organize legal Markdown safely" width="780">

I built Legal Markdown Organizer to organize legal Markdown files using filename rules and a supported subset of front matter. It previews file moves with dry-run, preserves document bytes and avoids overwriting existing destinations.

**Python standard library · pytest · GitHub Actions**

I also added local execution history and an undo preview for the latest eligible run. Undo restores only unchanged documents and refuses to overwrite existing files.

[Code & quick start](https://github.com/LuizChockt/legal-markdown-organizer#quick-start) · [Fictional examples](https://github.com/LuizChockt/legal-markdown-organizer/tree/main/examples) · [CI](https://github.com/LuizChockt/legal-markdown-organizer/actions/workflows/tests.yml)

### Web projects

I revisited earlier learning projects and improved them with responsive interfaces, a clearer separation of application logic and Node.js tests.

- **[JavaScript Calculator](https://github.com/LuizChockt/CalculadoraAprendizadoJS)** — arithmetic parser, keyboard input and session history. [Live demo](https://luizchockt.github.io/CalculadoraAprendizadoJS/).
- **[School Grade Calculator](https://github.com/LuizChockt/Media-Escolar-Calc)** — weighted averages, input validation and configurable thresholds. [Live demo](https://luizchockt.github.io/Media-Escolar-Calc/).

## Tools I use

**Python · JavaScript · HTML · CSS · Git · Markdown**

I use **pytest** for Python tests, **Node.js's test runner** for web logic, and **GitHub Actions** for continuous integration.

## How I build

- I separate parsing, rules and filesystem operations so I can test each part independently.
- I test real CLI entry points, edge cases and filesystem behavior with synthetic fixtures.
- I document working commands, scope and limitations alongside the code.
- I keep document processing local and dependencies proportional to the task.

I currently focus on practical automation, desktop and command-line tools, and clear web interfaces.

[Browse repositories](https://github.com/LuizChockt?tab=repositories) · [Background & profile maintenance](./docs/MAINTENANCE.md)
