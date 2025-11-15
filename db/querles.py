CREATE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        time TEXT NOT NULL
    )
"""

INSERT_TASK = "INSERT INTO tasks (task, time) VALUES (?, ?)"

SELECT_TASK = "SELECT id, task, time FROM tasks"

UPDATE_TASK = "UPDATE tasks SET task = ?, time = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"

