# Heroes API

Uma API para gerenciar heróis, oferecendo funcionalidades de criação, leitura, atualização e exclusão (CRUD). Este projeto utiliza tecnologias modernas como FastAPI, SQLModel e PostgreSQL, com suporte para migrações e testes automatizados.

---

## **Sumário**

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Endpoints](#endpoints)
- [Testes](#testes)

---

## **Requisitos**

- **Python 3.10 ou superior**
- **Docker** (opcional para PostgreSQL)
- **Poetry** para gerenciamento de dependências

---

## **Instalação**

1. Clone o repositório:
   ```bash
   git clone https://github.com/lealgabriel/Heroes-app-api
   cd heroes-api
   ```

2. Instale as dependências com Poetry:
   ```bash
   poetry install
   ```

---

## **Configuração**

Edite o arquivo `.env` para configurar as variáveis de ambiente. Exemplo:

```env
# BASE
API_V1_PREFIX="/api/v1"
DEBUG=True
PROJECT_NAME="Heroes App (local)"
VERSION="0.1.0"
DESCRIPTION="The API for Heroes app."

# BANCO DE DADOS
DB_ASYNC_CONNECTION_STR="postgresql+asyncpg://hero:heroPass123@localhost:5432/heroes_db"
DB_SYNC_CONNECTION_STR="postgresql+psycopg2://hero:heroPass123@localhost:5432/heroes_db"
DB_ASYNC_TEST_CONNECTION_STR="postgresql+asyncpg://hero:heroPass123@localhost:5436/heroes_db_tests"
```

---

## **Execução**

1. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Acesse a documentação interativa:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


---

## **Endpoints**

| Método | Endpoint           | Descrição                     |
|--------|--------------------|-----------------------------|
| POST   | `/heroes`          | Cria um novo herói           |
| GET    | `/heroes/{hero_id}`| Busca um herói por ID        |
| PATCH  | `/heroes/{hero_id}`| Atualiza dados de um herói    |
| DELETE | `/heroes/{hero_id}`| Remove um herói do sistema    |

---

## **Testes**

Execute os testes automatizados:

1. Rode todos os testes:
   ```bash
   pytest
   ```

2. Rode um teste específico:
   ```bash
   pytest tests/test_heroes.py::test_create_hero
   ```

---

## **Licença**

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

