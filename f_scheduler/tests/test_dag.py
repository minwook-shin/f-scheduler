import unittest

from f_scheduler import DefaultFunctionOperator
from f_scheduler.modules.dag import DAG


class TestDAG(unittest.TestCase):
    def setUp(self):
        self.dag = DAG()
        self.f = DefaultFunctionOperator(function=print, param=(['hello']), task_id='hello_task')
        self.f_2 = DefaultFunctionOperator(function=print, param=(['bye']), task_id='bye_task')

    def test_add_task(self):
        self.dag.add_task(self.f)
        self.assertIn('hello_task', self.dag.tasks)

    def test_set_downstream(self):
        self.dag.add_task(self.f)
        self.dag.add_task(self.f_2)
        self.dag.set_downstream('hello_task', 'bye_task')
        self.assertEqual(self.dag.tasks['hello_task'].next_task, self.dag.tasks['bye_task'])

    def test_run(self):
        self.dag.add_task(self.f)
        with self.assertRaises(Exception):
            self.dag.run('task1')

    def test_run_with_nonexistent_task(self):
        with self.assertRaises(KeyError):
            self.dag.run('nonexistent_task')

    def test_set_downstream_with_nonexistent_task(self):
        self.dag.add_task(self.f)
        with self.assertRaises(KeyError):
            self.dag.set_downstream('hello_task', 'nonexistent_task')


if __name__ == '__main__':
    unittest.main()
