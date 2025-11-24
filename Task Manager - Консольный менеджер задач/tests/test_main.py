"""
Тесты для менеджера задач
"""
import unittest
import os
import sys

# Добавляем src в путь для импорта
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import load_tasks, save_tasks

class TestTaskManager(unittest.TestCase):
    """Тесты менеджера задач"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.test_file = "data/test_tasks.json"
        self.tasks = [{"id": 1, "task": "Тестовая задача", "completed": False}]
    
    def test_save_and_load_tasks(self):
        """Тест сохранения и загрузки задач"""
        save_tasks(self.tasks)
        loaded_tasks = load_tasks()
        self.assertEqual(loaded_tasks, self.tasks)

if __name__ == "__main__":
    unittest.main()