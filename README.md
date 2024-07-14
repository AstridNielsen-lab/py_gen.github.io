```markdown
# Projeto Adega

Este projeto é um sistema de gerenciamento de adega, desenvolvido em Python com Flask e SQLite.
O objetivo é facilitar o controle de estoque, vendas, entradas e saídas de produtos em uma adega.

## Funcionalidades

Gerenciamento de Estoque: Adicione, visualize e atualize produtos em estoque.
Registro de Vendas: Registre vendas de produtos e atualize o estoque automaticamente.
Controle de Entradas e Saídas: Gerencie entradas e saídas de produtos, com relatórios detalhados.
Dashboard* Visualize informações sobre o estoque e vendas em um painel intuitivo.
```

## Estrutura do Projeto

```plaintext
/adega
│
├── app.py               # Arquivo principal do aplicativo Flask
├── database.py          # Inicialização e configuração do banco de dados
├── templates/           # Pasta contendo os templates HTML
│   ├── index.html       # Página inicial
│   ├── prod.html        # Página de produtos
│   ├── instrucoes.html   # Página de instruções
│   ├── ...              # Outras páginas
└── static/              # Pasta para arquivos estáticos (CSS, JS, etc.)
```

## Pré-requisitos

Antes de executar o projeto, você precisará ter o Python instalado e configurar um ambiente virtual. Use os seguintes comandos:

```bash
# Clone o repositório
git clone https://github.com/AstridNielsen-lab/py_gen.github.io.git
cd py_gen.github.io

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Para Linux/Mac
.\.venv\Scripts\activate   # Para Windows

# Instale as dependências
pip install -r requirements.txt
```

## Executando o Projeto

Para rodar o aplicativo, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

O aplicativo estará disponível em `http://127.0.0.1:5000/`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

![Tela](https://raw.githubusercontent.com/AstridNielsen-lab/py_gen.github.io/main/capa.png)

![Código](https://raw.githubusercontent.com/AstridNielsen-lab/py_gen.github.io/main/prod.png)

![Código](https://raw.githubusercontent.com/AstridNielsen-lab/py_gen.github.io/main/estoque.png)
