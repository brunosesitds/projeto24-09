# Gerenciador de Tarefas (Tkinter)

Projeto simples de um aplicativo desktop em Python usando Tkinter.

Funcionalidades:
- CRUD de tarefas (cadastrar, listar, editar, excluir)
- Pesquisa por título/descrição
- Persistência em SQLite (arquivo `projeto_tkinter.db`)

Estrutura:
- `main.py` - ponto de entrada
- `interface.py` - interface Tkinter
- `dados.py` - operações com o banco SQLite
- `validacoes.py` - validações simples

Como executar:

```bash
python main.py
```

Notas:
- Projeto usa apenas bibliotecas padrão (Tkinter, sqlite3).
- Para empacotar, gere um ZIP incluindo os arquivos e o banco de dados.
