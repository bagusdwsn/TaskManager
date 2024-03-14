import json

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def complete(self):
        self.completed = True

    def __str__(self):
        return f"{self.name} - {'Completed' if self.completed else 'Incomplete'}"

class TaskFactory:
    @staticmethod
    def create_task(name):
        return Task(name)

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        task = TaskFactory.create_task(name)
        self.tasks.append(task)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()

    def list_tasks(self):
        return self.tasks

    def delete_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.completed]

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            task_list = [{'name': task.name, 'completed': task.completed} for task in self.tasks]
            json.dump(task_list, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tasks = [Task(task['name'], task['completed']) for task in data]
        except FileNotFoundError:
            # Handle the case where the file does not exist
            print("File not found. No tasks loaded.")
