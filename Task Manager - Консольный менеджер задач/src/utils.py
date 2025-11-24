"""
Вспомогательные функции для менеджера задач
"""
import json
import os

DATA_FILE = "data/tasks.json"

def load_tasks():
    """Загружает задачи из файла"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Сохраняет задачи в файл"""
    # Создаем папку data, если её нет
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def display_tasks(tasks):
    """Отображает список задач"""
    if not tasks:
        print("Нет задач!")
        return
    
    print("\n=== Ваши задачи ===")
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"{task['id']}. [{status}] {task['task']}")