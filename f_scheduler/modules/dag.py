class DAG:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def set_downstream(self, task_id, next_task_id):
        task = self.tasks[task_id]
        next_task = self.tasks[next_task_id]
        task.next(next_task)

    def run(self, start_task_id):
        start_task = self.tasks[start_task_id]
        start_task.run()
