import sqlite3
from typing import List, Dict, Optional


DB_PATH = 'projeto_tkinter.db'


def init_db(path: str = DB_PATH):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority INTEGER DEFAULT 3,
            status TEXT DEFAULT 'pendente'
        )
        '''
    )
    conn.commit()
    conn.close()


def create_task(task: Dict, path: str = DB_PATH) -> int:
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
        (task.get('title'), task.get('description'), task.get('priority', 3), task.get('status', 'pendente'))
    )
    conn.commit()
    task_id = cur.lastrowid
    conn.close()
    return task_id


def read_tasks(filter_text: Optional[str] = None, path: str = DB_PATH) -> List[Dict]:
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    if filter_text:
        q = '%' + filter_text + '%'
        cur.execute('SELECT id, title, description, priority, status FROM tasks WHERE title LIKE ? OR description LIKE ? ORDER BY id', (q, q))
    else:
        cur.execute('SELECT id, title, description, priority, status FROM tasks ORDER BY id')
    rows = cur.fetchall()
    conn.close()
    return [dict(id=r[0], title=r[1], description=r[2], priority=r[3], status=r[4]) for r in rows]


def update_task(task_id: int, updates: Dict, path: str = DB_PATH) -> None:
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute(
        'UPDATE tasks SET title = ?, description = ?, priority = ?, status = ? WHERE id = ?',
        (updates.get('title'), updates.get('description'), updates.get('priority', 3), updates.get('status', 'pendente'), task_id)
    )
    conn.commit()
    conn.close()


def delete_task(task_id: int, path: str = DB_PATH) -> None:
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
