import tkinter as tk
from tkinter import ttk, messagebox
from dados import init_db, create_task, read_tasks, update_task, delete_task
from validacoes import validar_titulo, normalizar_prioridade


class TaskApp:
    def __init__(self):
        init_db()
        self.root = tk.Tk()
        self.root.title('Gerenciador de Tarefas - SENAI')
        self.setup_ui()

    def setup_ui(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.pack(fill=tk.BOTH, expand=True)

        # Entry fields
        lbl_title = ttk.Label(frm, text='Título')
        lbl_title.grid(row=0, column=0, sticky=tk.W)
        self.ent_title = ttk.Entry(frm, width=40)
        self.ent_title.grid(row=0, column=1, columnspan=3, sticky=tk.W)

        lbl_prio = ttk.Label(frm, text='Prioridade (1-5)')
        lbl_prio.grid(row=1, column=0, sticky=tk.W)
        self.ent_prio = ttk.Entry(frm, width=5)
        self.ent_prio.insert(0, '3')
        self.ent_prio.grid(row=1, column=1, sticky=tk.W)

        lbl_desc = ttk.Label(frm, text='Descrição')
        lbl_desc.grid(row=2, column=0, sticky=tk.NW)
        self.txt_desc = tk.Text(frm, width=50, height=5)
        self.txt_desc.grid(row=2, column=1, columnspan=3, sticky=tk.W)

        # Buttons
        btn_add = ttk.Button(frm, text='Adicionar', command=self.on_add)
        btn_add.grid(row=3, column=1, sticky=tk.W, pady=6)
        btn_update = ttk.Button(frm, text='Atualizar', command=self.on_update)
        btn_update.grid(row=3, column=2, sticky=tk.W)
        btn_delete = ttk.Button(frm, text='Excluir', command=self.on_delete)
        btn_delete.grid(row=3, column=3, sticky=tk.W)

        # Search
        lbl_search = ttk.Label(frm, text='Pesquisar')
        lbl_search.grid(row=4, column=0, sticky=tk.W)
        self.ent_search = ttk.Entry(frm, width=30)
        self.ent_search.grid(row=4, column=1, sticky=tk.W)
        btn_search = ttk.Button(frm, text='Buscar', command=self.on_search)
        btn_search.grid(row=4, column=2, sticky=tk.W)
        btn_clear = ttk.Button(frm, text='Limpar', command=self.on_clear)
        btn_clear.grid(row=4, column=3, sticky=tk.W)

        # Treeview
        cols = ('id', 'title', 'priority', 'status')
        self.tree = ttk.Treeview(frm, columns=cols, show='headings', height=8)
        self.tree.heading('id', text='ID')
        self.tree.heading('title', text='Título')
        self.tree.heading('priority', text='Prioridade')
        self.tree.heading('status', text='Status')
        self.tree.column('id', width=50)
        self.tree.column('title', width=300)
        self.tree.column('priority', width=80)
        self.tree.column('status', width=100)
        self.tree.grid(row=5, column=0, columnspan=4, pady=8)
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        self.refresh_list()

    def run(self):
        self.root.mainloop()

    def _read_fields(self):
        title = self.ent_title.get().strip()
        desc = self.txt_desc.get('1.0', tk.END).strip()
        prio = normalizar_prioridade(self.ent_prio.get())
        return dict(title=title, description=desc, priority=prio, status='pendente')

    def on_add(self):
        task = self._read_fields()
        if not validar_titulo(task['title']):
            messagebox.showwarning('Validação', 'Título inválido (mínimo 2 caracteres).')
            return
        create_task(task)
        messagebox.showinfo('Sucesso', 'Tarefa adicionada.')
        self.refresh_list()
        self.on_clear()

    def on_update(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Atualizar', 'Selecione uma tarefa para atualizar.')
            return
        item = self.tree.item(sel[0])
        task_id = int(item['values'][0])
        updates = self._read_fields()
        if not validar_titulo(updates['title']):
            messagebox.showwarning('Validação', 'Título inválido.')
            return
        update_task(task_id, updates)
        messagebox.showinfo('Sucesso', 'Tarefa atualizada.')
        self.refresh_list()

    def on_delete(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning('Excluir', 'Selecione uma tarefa para excluir.')
            return
        item = self.tree.item(sel[0])
        task_id = int(item['values'][0])
        if not messagebox.askyesno('Confirmar', 'Confirma exclusão da tarefa?'):
            return
        delete_task(task_id)
        messagebox.showinfo('Sucesso', 'Tarefa excluída.')
        self.refresh_list()

    def on_search(self):
        q = self.ent_search.get().strip()
        self.refresh_list(filter_text=q)

    def on_clear(self):
        self.ent_title.delete(0, tk.END)
        self.ent_prio.delete(0, tk.END)
        self.ent_prio.insert(0, '3')
        self.txt_desc.delete('1.0', tk.END)
        self.ent_search.delete(0, tk.END)
        self.refresh_list()

    def refresh_list(self, filter_text: str = None):
        for r in self.tree.get_children():
            self.tree.delete(r)
        rows = read_tasks(filter_text)
        for t in rows:
            self.tree.insert('', tk.END, values=(t['id'], t['title'], t['priority'], t['status']))

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        item = self.tree.item(sel[0])
        vals = item['values']
        # id, title, priority, status
        self.ent_title.delete(0, tk.END)
        self.ent_title.insert(0, vals[1])
        self.ent_prio.delete(0, tk.END)
        self.ent_prio.insert(0, vals[2])
        # load description from DB
        from dados import read_tasks
        rows = read_tasks()
        for r in rows:
            if r['id'] == int(vals[0]):
                self.txt_desc.delete('1.0', tk.END)
                self.txt_desc.insert('1.0', r['description'] or '')
                break
