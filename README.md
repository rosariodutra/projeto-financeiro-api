# 💰 API Financeira

API REST desenvolvida em Python com FastAPI para gerenciamento de usuários e transações financeiras.

O projeto foi desenvolvido com foco em autenticação, autorização, validação de dados, isolamento de informações por usuário e boas práticas de desenvolvimento de APIs.

---

## 🚀 Tecnologias

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Alembic
- JWT
- Passlib
- Pytest
- Git
- GitHub
- Swagger / OpenAPI

---

## 📌 Funcionalidades

### 👤 Usuários

- Cadastro de usuários
- Validação de e-mail
- Hash seguro de senhas
- Login com autenticação JWT
- Validação de token

### 💰 Transações

- Criar transações
- Listar transações
- Filtrar transações por tipo
- Atualizar transações
- Excluir transações
- Vincular transações ao usuário autenticado

### 📊 Resumo financeiro

- Total de entradas
- Total de saídas
- Cálculo do saldo
- Isolamento dos dados por usuário

### 🔐 Segurança

- Autenticação utilizando JWT
- Senhas armazenadas com hash
- Proteção de endpoints
- Controle de acesso por usuário
- Usuários não podem alterar ou excluir transações pertencentes a outros usuários
- Resumo financeiro isolado por usuário

---

## 🧪 Testes automatizados

O projeto possui testes automatizados utilizando Pytest.

Atualmente são realizados **7 testes**, incluindo:

- Validação de valores positivos
- Rejeição de valores iguais a zero
- Rejeição de valores negativos
- Bloqueio de acesso sem autenticação
- Proteção contra alteração de transações de outros usuários
- Proteção contra exclusão de transações de outros usuários
- Isolamento do resumo financeiro por usuário

Para executar os testes:

```bash
pytest
```

Resultado esperado:

```text
7 passed
```

---

## 📖 Documentação da API

Após iniciar a aplicação, a documentação interativa pode ser acessada pelo Swagger:

```text
http://127.0.0.1:8000/docs
```

Também é possível acessar a documentação OpenAPI:

```text
http://127.0.0.1:8000/redoc
```

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/rosariodutra/projeto-financeiro-api.git
```

### 2. Entrar na pasta

```bash
cd projeto-financeiro-api
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install fastapi uvicorn sqlalchemy alembic passlib bcrypt python-jose pytest httpx
```

### 6. Executar a API

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 🗄️ Banco de dados

O projeto utiliza SQLite como banco de dados.

As alterações estruturais do banco são gerenciadas utilizando Alembic.

Para aplicar as migrações:

```bash
alembic upgrade head
```

---

## 🧪 Estrutura dos testes

Os testes estão organizados na pasta:

```text
tests/
├── conftest.py
├── test_transacoes.py
└── test_validacoes.py
```

O ambiente de testes utiliza um banco SQLite separado em memória, evitando alterações no banco de dados utilizado pela aplicação.

---

## 📂 Estrutura do projeto

```text
projeto-financeiro-api/
│
├── alembic/
│   └── versions/
│
├── tests/
│   ├── conftest.py
│   ├── test_transacoes.py
│   └── test_validacoes.py
│
├── .gitignore
├── alembic.ini
├── database.py
├── main.py
├── models.py
├── schemas.py
├── security.py
├── pytest.ini
└── README.md
```

---

## 💡 Competências demonstradas

Este projeto demonstra conhecimentos práticos em:

- Desenvolvimento de APIs REST com Python e FastAPI
- Modelagem de dados com SQLAlchemy
- Validação de dados com Pydantic
- Autenticação e autorização utilizando JWT
- Hash e verificação segura de senhas
- Controle de acesso baseado no usuário autenticado
- Implementação de operações CRUD
- Gerenciamento de banco de dados com SQLite
- Controle de versões de banco de dados com Alembic
- Tratamento de exceções HTTP
- Documentação de APIs com Swagger/OpenAPI
- Testes automatizados com Pytest
- Controle de qualidade e validação de regras de negócio
- Versionamento de código com Git e GitHub

---

## 🎯 Objetivo do projeto

Projeto desenvolvido para consolidar conhecimentos em desenvolvimento backend com Python, APIs REST, bancos de dados, autenticação, segurança, testes automatizados e controle de versão.

O projeto também faz parte do portfólio profissional para demonstração de conhecimentos práticos em desenvolvimento de software.

---

## 👩‍💻 Autora

**Rosário Dutra**

Projeto desenvolvido para estudos e portfólio profissional.