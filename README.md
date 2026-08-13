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

## 🧪 Testes realizados

A API foi testada utilizando o Swagger UI, incluindo cenários de sucesso, validação, autenticação e controle de acesso.

### Validação de dados

| Cenário | Resultado |
|---|---:|
| Valor igual a `0` | 422 ✅ |
| Valor negativo | 422 ✅ |
| Descrição vazia | 422 ✅ |
| Tipo de transação inválido | 422 ✅ |
| Data em formato inválido | 422 ✅ |

### Autenticação e autorização

| Cenário | Resultado |
|---|---:|
| Requisição sem token JWT | 401 ✅ |
| Token JWT inválido | 401 ✅ |
| Usuário acessando transação de outro usuário | 404 ✅ |
| Usuário tentando atualizar transação de outro usuário | 404 ✅ |
| Usuário tentando excluir transação de outro usuário | 404 ✅ |
| Usuário consultando suas próprias transações | 200 ✅ |

### Operações da API

| Operação | Resultado |
|---|---:|
| Criação de usuário | 201 ✅ |
| Criação de transação | 201 ✅ |
| Listagem de transações | 200 ✅ |
| Atualização autorizada | 200 ✅ |
| Exclusão autorizada | 200 ✅ |

## 📌 Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/usuarios` | Cria um novo usuário |
| POST | `/login` | Realiza autenticação e retorna o token JWT |
| POST | `/transacoes` | Cria uma nova transação |
| GET | `/transacoes` | Lista as transações do usuário autenticado |
| PUT | `/transacoes/{id}` | Atualiza uma transação do usuário autenticado |
| DELETE | `/transacoes/{id}` | Exclui uma transação do usuário autenticado |
| GET | `/resumo` | Retorna o resumo financeiro |
| GET | `/` | Retorna a resposta inicial da API |

🎯 Objetivo do projeto

Projeto desenvolvido para prática e demonstração de conhecimentos em desenvolvimento de APIs REST com Python, autenticação, persistência de dados, validação, segurança e documentação de APIs.
