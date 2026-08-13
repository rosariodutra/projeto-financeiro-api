API Financeira

API REST desenvolvida em Python com FastAPI para gerenciamento de usuários e transações financeiras.

O projeto possui autenticação com JWT, controle de acesso por usuário, validação de dados, persistência com SQLAlchemy e gerenciamento de migrações com Alembic.

🚀 Tecnologias
Python
FastAPI
Pydantic
SQLAlchemy
SQLite
Alembic
JWT
Passlib / bcrypt
Swagger / OpenAPI
🔐 Segurança

A API utiliza autenticação baseada em JWT (JSON Web Token).

Cada usuário autenticado possui acesso somente às suas próprias transações.

Foram implementadas verificações para impedir que um usuário:

consulte uma transação de outro usuário;
altere uma transação de outro usuário;
exclua uma transação de outro usuário.

Também são rejeitados tokens ausentes ou inválidos.

📋 Validações

A API realiza validações dos dados enviados, incluindo:

valor maior que zero;
descrição não vazia;
tipo de transação válido;
formato de data válido;
autenticação obrigatória nos endpoints protegidos.
📂 Estrutura do projeto
projeto-financeiro-api/
│
├── alembic/
│   └── versions/
│
├── .gitignore
├── alembic.ini
├── database.py
├── main.py
├── models.py
├── schemas.py
└── security.py
⚙️ Como executar

Clone o repositório:

git clone https://github.com/rosariodutra/projeto-financeiro-api.git

Entre na pasta:

cd projeto-financeiro-api

Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual no Windows:

venv\Scripts\activate

Instale as dependências necessárias:

pip install fastapi uvicorn sqlalchemy pydantic passlib bcrypt python-jose alembic

Execute a aplicação:

uvicorn main:app --reload
📖 Documentação

Após iniciar a aplicação, a documentação interativa pode ser acessada em:

http://127.0.0.1:8000/docs

A documentação é disponibilizada pelo Swagger UI, permitindo testar os endpoints diretamente pelo navegador.

🔑 Autenticação

Para utilizar os endpoints protegidos:

Realize o login.
Obtenha o token JWT.
Clique em Authorize no Swagger.
Informe o token no formato:
Bearer SEU_TOKEN

Após a autenticação, os endpoints protegidos poderão ser utilizados de acordo com as permissões do usuário.

💰 Transações

A API permite operações como:

criação de transações;
consulta de transações;
atualização;
exclusão;
listagem das transações do usuário autenticado.

As operações de consulta, alteração e exclusão respeitam o usuário associado à transação.

🗃️ Banco de dados e migrações

O projeto utiliza SQLite como banco de dados e Alembic para controle de migrações.

O arquivo do banco de dados local não é versionado no GitHub, conforme definido no .gitignore.

🧪 Testes realizados

Durante o desenvolvimento foram realizados testes utilizando o Swagger, incluindo:

criação de usuário;
autenticação;
geração e validação de JWT;
criação de transações;
consulta de transações;
atualização de transações;
exclusão de transações;
tentativa de acesso entre usuários;
validação de valores;
validação de descrição;
validação do tipo;
validação de data;
acesso sem autenticação;
acesso com token inválido.
🎯 Objetivo do projeto

Projeto desenvolvido para prática e demonstração de conhecimentos em desenvolvimento de APIs REST com Python, autenticação, persistência de dados, validação, segurança e documentação de APIs.