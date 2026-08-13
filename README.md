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