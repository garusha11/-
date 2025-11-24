"""
Главный модуль приложения - Менеджер задач
"""

from utils import load_tasks, save_tasks, display_tasks

def main():
    """Основная функция приложения"""
    print("=== Менеджер задач ===")
    
    tasks = load_tasks()
    
    while True:
        print("\n1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")
        
        choice = input("\nВыберите действие: ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task = input("Введите задачу: ")
            tasks.append({"id": len(tasks) + 1, "task": task, "completed": False})
            save_tasks(tasks)
            print("Задача добавлена!")
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                tasks = [t for t in tasks if t["id"] != task_id]
                save_tasks(tasks)
                print("Задача удалена!")
            except ValueError:
                print("Ошибка: введите число!")
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()