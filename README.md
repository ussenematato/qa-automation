# QA Automation Project

Estrutura base para automação de testes com Python, Selenium e Pytest.

## Estrutura

- `pages/`: page objects
- `tests/`: testes automatizados
- `data/`: arquivos de dados (JSON, CSV, etc.)
- `conftest.py`: fixtures globais do pytest
- `pytest.ini`: configuração do pytest
- `requirements.txt`: dependências do projeto

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução

```bash
pytest
```

## Exemplo

O projeto inclui um exemplo de Page Object Model para login, pronto para ser adaptado ao seu site real.
