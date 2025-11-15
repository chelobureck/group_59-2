import sqlite3
from db import querles
from config import path_db
from typing import Any

def init_db() -> None:
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(querles.CREATE_TASKS)
    print("База данных успешно инициализирована!")
    conn.commit()
    conn.close()

def add_task(task: str | None) -> int:
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(querles.INSERT_TASK, (task, ))
    conn.commit()
    task_id = cursor.rowcount
    conn.close()
    return task_id

def get_tasks() -> list:
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(querles.SELECT_TASK)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(id: int, task: str | None) -> None:
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(querles.UPDATE_TASK, (task, id))
    conn.commit()
    conn.close()

def delete_task(id: int) -> None:
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(querles.DELETE_TASK, (id, ))
    conn.commit()
    conn.close()

