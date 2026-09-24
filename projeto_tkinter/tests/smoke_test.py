import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dados import create_task, delete_task, init_db, read_tasks, update_task


def run_smoke():
    print('Inicializando DB...')
    init_db()

    # Garante banco limpo para o teste de fumaça.
    for task in read_tasks():
        delete_task(task['id'])

    print('Criando tarefa...')
    tid = create_task({'title': 'Teste', 'description': 'Descrição de teste', 'priority': 2, 'status': 'pendente'})
    print('ID criado:', tid)

    tasks = read_tasks()
    print('Tarefas lidas:', tasks)

    print('Atualizando tarefa...')
    update_task(tid, {'title': 'Teste alterado', 'description': 'Alterado', 'priority': 1, 'status': 'concluida'})
    tasks = read_tasks()
    print('Depois da atualização:', tasks)

    print('Excluindo tarefa...')
    delete_task(tid)
    tasks = read_tasks()
    print('Depois da exclusão (deve estar vazio):', tasks)


if __name__ == '__main__':
    run_smoke()
