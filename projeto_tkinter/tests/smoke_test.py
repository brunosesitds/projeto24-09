from dados import init_db, create_task, read_tasks, update_task, delete_task


def run_smoke():
    print('Inicializando DB...')
    init_db()
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
