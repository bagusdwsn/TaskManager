import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from tasks.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        task_manager = TaskManager()
        task_manager.add_task("Task 1")
        self.assertEqual(len(task_manager.list_tasks()), 1)

    def test_complete_task(self):
        task_manager = TaskManager()
        task_manager.add_task("Task 1")
        task_manager.complete_task(0)
        self.assertTrue(task_manager.list_tasks()[0].completed)

if __name__ == "__main__":
    unittest.main()
