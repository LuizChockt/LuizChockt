<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/identity/profile-octocat.webp">
  <source media="(prefers-color-scheme: light)" srcset="./assets/identity/profile-light-premium.webp">
  <img src="./assets/identity/profile-octocat.webp" alt="Luiz Chockt — identidade de desenvolvimento de software, Python e automação." width="1200">
</picture>

**Idioma:** [English](./README.md) · Português (Brasil)

[Projetos](#projetos-em-destaque) · [Repositórios](https://github.com/LuizChockt?tab=repositories)

# Olá, sou o Luiz.

Desenvolvo **ferramentas Python para Markdown, organização de arquivos e automação**, além de projetos web com **JavaScript, HTML e CSS**.

Sou formado em Análise e Desenvolvimento de Sistemas e moro no Brasil. Minha formação e experiência em Direito trazem problemas práticos para resolver com software: documentos, informações e trabalho repetitivo.

## Projetos em destaque

### [ClipInbox](https://github.com/LuizChockt/clipinbox)

<img src="https://raw.githubusercontent.com/LuizChockt/clipinbox/main/assets/identity/cover-premium.webp" alt="ClipInbox — captura da área de transferência para Markdown" width="780">

Criei o ClipInbox para salvar textos da área de transferência em uma caixa de entrada Markdown local, por meio de um atalho global no Windows. Ele também permite registrar notas rápidas pela bandeja do sistema, sem abrir o Obsidian.

**Python · Tkinter · Win32 · pytest · GitHub Actions**

[Download para Windows](https://github.com/LuizChockt/clipinbox/releases/tag/v0.1.0) · [CI](https://github.com/LuizChockt/clipinbox/actions/workflows/ci-release.yml)

### [Markdown Link Auditor](https://github.com/LuizChockt/markdown-link-auditor)

<img src="https://raw.githubusercontent.com/LuizChockt/markdown-link-auditor/main/assets/identity/cover-premium.webp" alt="Markdown Link Auditor — auditoria de links e anexos em Markdown" width="780">

Desenvolvi o Markdown Link Auditor para identificar referências locais quebradas, anexos ausentes, links ambíguos e possíveis notas órfãs em bases de conhecimento Markdown. Ele reconhece links CommonMark e wikilinks do Obsidian e gera relatórios determinísticos em texto e JSON.

**Python · markdown-it-py · pytest · GitHub Actions**

A análise não altera os arquivos, resolve caminhos com caracteres Unicode e respeita limites explícitos de acesso ao sistema de arquivos. O programa contabiliza URLs externas sem realizar consultas HTTP.

[Código e início rápido](https://github.com/LuizChockt/markdown-link-auditor#quick-start) · [Relatório de exemplo](https://github.com/LuizChockt/markdown-link-auditor/blob/main/examples/reports/sample-report.txt) · [CI](https://github.com/LuizChockt/markdown-link-auditor/actions/workflows/tests.yml)

### [Legal Markdown Organizer](https://github.com/LuizChockt/legal-markdown-organizer)

<img src="https://raw.githubusercontent.com/LuizChockt/legal-markdown-organizer/main/assets/identity/cover-premium.webp" alt="Legal Markdown Organizer — organização segura de documentos jurídicos em Markdown" width="780">

Criei o Legal Markdown Organizer para organizar arquivos jurídicos em Markdown com regras de nomenclatura e um subconjunto de metadados front matter. Ele permite simular movimentações com dry-run, preserva os bytes dos documentos e evita sobrescrever destinos existentes.

**Biblioteca padrão Python · pytest · GitHub Actions**

Também implementei o histórico local de execuções e a prévia de desfazer a última execução elegível. A operação só restaura documentos que não foram modificados e recusa sobrescrever arquivos existentes.

[Código e início rápido](https://github.com/LuizChockt/legal-markdown-organizer#quick-start) · [Exemplos fictícios](https://github.com/LuizChockt/legal-markdown-organizer/tree/main/examples) · [CI](https://github.com/LuizChockt/legal-markdown-organizer/actions/workflows/tests.yml)

### Projetos web

Retomei projetos anteriores de aprendizagem e os aprimorei com interfaces responsivas, separação da lógica da aplicação e testes com Node.js.

- **[Calculadora JavaScript](https://github.com/LuizChockt/CalculadoraAprendizadoJS)** — parser aritmético, entrada por teclado e histórico da sessão. [Demonstração](https://luizchockt.github.io/CalculadoraAprendizadoJS/).
- **[Calculadora de Média Escolar](https://github.com/LuizChockt/Media-Escolar-Calc)** — médias ponderadas, validação de entradas e critérios configuráveis. [Demonstração](https://luizchockt.github.io/Media-Escolar-Calc/).

## Ferramentas que utilizo

**Python · JavaScript · HTML · CSS · Git · Markdown**

Uso **pytest** para testar programas Python, **o executor de testes do Node.js** para a lógica dos projetos web e **GitHub Actions** para integração contínua.

## Como desenvolvo

- Separo a interpretação de dados, as regras e as operações no sistema de arquivos para testar cada parte independentemente.
- Testo os pontos de entrada reais das ferramentas de linha de comando, os casos extremos e o comportamento do sistema de arquivos com dados fictícios.
- Documento os comandos executáveis, o escopo e as limitações junto ao código.
- Mantenho o processamento de documentos local e as dependências proporcionais ao problema.

Meu foco atual é automação prática, ferramentas desktop e de linha de comando, e interfaces web claras.

[Explorar repositórios](https://github.com/LuizChockt?tab=repositories) · [Manutenção do perfil](./docs/MAINTENANCE.md)
