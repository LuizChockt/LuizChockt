<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="./assets/banner-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="./assets/banner-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.svg">
  <img src="./assets/banner-light.svg" alt="Luiz Chockt — Python tools, automation, command-line tools and web development." width="1200">
</picture>

[Português brasileiro](./README.pt-BR.md) · [Projects](#selected-projects) · [Repositories](https://github.com/LuizChockt?tab=repositories)

# Hi, I'm Luiz.

I build **Python tools for Markdown, file organization and automation**, alongside web projects with **JavaScript, HTML and CSS**.

I'm a Systems Analysis and Development graduate based in Brazil. My background in law gives me a practical source of problems to solve with software: documents, information and repetitive work.

## Selected projects

### [Markdown Link Auditor](https://github.com/LuizChockt/markdown-link-auditor)

Find broken local references, missing attachments, ambiguous links and potential orphan notes in a Markdown knowledge base. Supports CommonMark and Obsidian wikilinks, with deterministic text and JSON reports.

**Python · markdown-it-py · pytest · GitHub Actions**

Read-only scanning, Unicode-aware resolution and explicit filesystem boundaries. External URLs are counted, without HTTP checks.

[Code & quick start](https://github.com/LuizChockt/markdown-link-auditor#quick-start) · [Sample report](https://github.com/LuizChockt/markdown-link-auditor/blob/main/examples/reports/sample-report.txt) · [CI](https://github.com/LuizChockt/markdown-link-auditor/actions/workflows/tests.yml)

### [Legal Markdown Organizer](https://github.com/LuizChockt/legal-markdown-organizer)

Organize legal Markdown files using filename rules and a supported subset of front matter. Preview moves with dry-run, preserve document bytes and avoid overwriting existing destinations.

**Python standard library · pytest · GitHub Actions**

A local CLI connecting legal document workflows with practical automation. Classification is deterministic; the tool does not interpret legal arguments or rewrite links.

[Code & quick start](https://github.com/LuizChockt/legal-markdown-organizer#quick-start) · [Fictional examples](https://github.com/LuizChockt/legal-markdown-organizer/tree/main/examples) · [CI](https://github.com/LuizChockt/legal-markdown-organizer/actions/workflows/tests.yml)

### Web projects

Earlier learning projects, developed further with responsive interfaces, separated application logic and Node.js tests.

- **[JavaScript Calculator](https://github.com/LuizChockt/CalculadoraAprendizadoJS)** — arithmetic parser, keyboard input and session history. [Live demo](https://luizchockt.github.io/CalculadoraAprendizadoJS/).
- **[School Grade Calculator](https://github.com/LuizChockt/Media-Escolar-Calc)** — weighted averages, input validation and configurable thresholds. [Live demo](https://luizchockt.github.io/Media-Escolar-Calc/).

## Tools I use

**Python · JavaScript · HTML · CSS · Git · Markdown**

**pytest** for Python behavior tests, **Node.js's test runner** for web logic, and **GitHub Actions** for continuous integration.

## How I build

- Separate parsing, rules and filesystem operations so each can be tested.
- Exercise real CLI entry points, edge cases and filesystem behavior with synthetic fixtures.
- Document working commands, scope and limitations alongside the code.
- Keep document processing local and dependencies proportional to the task.

My current focus is practical automation, CLI tools and clear web interfaces.

[Browse repositories](https://github.com/LuizChockt?tab=repositories) · [Background & profile maintenance](./docs/MAINTENANCE.md)
