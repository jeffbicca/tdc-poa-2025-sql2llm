# Workshop TDC-X 2025 POA: do SQL ao LLM - Transformando banco de dados em inteligência com MCP Toolbox

Este workshop tem como objetivo, apresentar uma técnica de integração entre bancos de dados SQL e modelos de linguagem (LLMs), com base no [MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox/) da Google.

A base de dados a ser utilizada é a [Chinook](https://www.sqlitetutorial.net/sqlite-sample-database/), uma base SQLite.

## Propósito

- Demonstrar como utilizar o MCP Toolbox for Databases para criar um agente que responda a prompts a partir de uma base de dados "real".
- Configurar e utilizar o VSCode com GitHub Copilot para desenvolver e testar a toolbox.
- Explorar o uso de prompts e automações para se trabalhar com dados.
- Escrever um client em JavaScript com LangChain para interagir com a toolbox.

## Pré-requisitos

- VSCode instalado ([Download](https://code.visualstudio.com/))
- MCP Toolbox for Databases ([Download](https://github.com/googleapis/genai-toolbox/releases/))
- Licença Github Copilot ativa

## Como subir o ambiente

1. Na pasta `.vscode`, abra o arquivo `mcp.json`
2. Ao abrir o arquivo, o VSCode já irá disponibilizar a opção de "Start" do MCP Server.

## Como testar o ambiente

1. Abra o arquivo `prompts.md`. Lá há alguns exemplos para ir se guiando.
2. Execute os prompts propostos no chat do Github Copilot e vá testando as tools disponíveis.

    2.1. Como recomendação, desabilite todas as demais tools do VSCode e deixe apenas a do sqlite/MCP Toolbox ativa. Para isto, clique no botão "Configure tools" (ao lado do botão "Enviar" do chat) e deixe apenas a toolbox `sqlite` marcada. 