# Proposta de Projeto - Gerenciador de Tarefas

Campo | Preenchimento da equipe
---|---
Nome do aplicativo|Gerenciador de Tarefas - SENAI
Problema que será resolvido|Organizar tarefas, priorizar, registrar descrição e manter histórico local.
Público usuário|Estudantes e pequenos profissionais que precisam controlar atividades diárias.
Dados que serão armazenados|Título, descrição, prioridade (1-5), status (pendente/concluída), id.
Funcionalidades principais|Cadastrar, listar, pesquisar, editar, excluir, persistir dados localmente em SQLite.
Telas ou seções previstas|Formulário de cadastro/edição, lista com pesquisa, confirmações e mensagens.
Forma de persistência|SQLite embarcado (arquivo `projeto_tkinter.db`).
Maior risco técnico|Testes de persistência e tratamento de concorrência; minimizar com transações simples.
Divisão de responsabilidades|Único desenvolvedor: interface, dados, validação e documentação.
