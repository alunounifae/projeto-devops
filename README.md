# TaskAPI

Uma API voltada para gerenciamento de tarefas

## Autores

- Lucas André
- Marco Antônio
- Breno Henrique
- Thiago Luís

## Funcionalidades

- CRUD de Tarefas

## Stack utilizada

**Back-end:** Python, FastAPI, Uvicorn (Local), Gunicorn (Cloud)

**Cloud:** Google Cloud

**Banco de Dados:** PostgreSQL com NeonDB (produção), SQLITE (testes)

**CI/CD**: GitHub Actions

- Integração automática de código-fonte atualizado
- Instalação de dependências necessárias
- Execução de testes após transferência de dados para a branch principal
- Dependabot para automatizar a validação das versões das dependências do projeto
- Biblioteca bandit para verificar segurança do código
- Biblioteca flake8 para verificar formatação do código
- Biblioteca black para formatação automática do código

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/alunounifae/projeto-devops
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  uvicorn task_api.app.main:app --reload --port 8080
```

Rodar os testes

```bash
  pytest
```
