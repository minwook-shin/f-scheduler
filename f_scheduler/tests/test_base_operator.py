import unittest
from unittest.mock import Mock
from f_scheduler.operators.base_op import BaseOperator


class TestBaseOperator(unittest.TestCase):
    def setUp(self):
        self.base_operator = BaseOperator('task1')

    def test_successful_execution_leads_to_next_task(self):
        next_task_mock = Mock()
        self.base_operator.next(next_task_mock)
        self.base_operator.execute = Mock(return_value=True)
        self.base_operator.run()
        next_task_mock.run.assert_called_once()

    def test_unsuccessful_execution_does_not_lead_to_next_task(self):
        next_task_mock = Mock()
        self.base_operator.next(next_task_mock)
        self.base_operator.execute = Mock(return_value=False)
        self.base_operator.run()
        next_task_mock.run.assert_not_called()

    def test_execution_without_next_task(self):
        self.base_operator.execute = Mock(return_value=True)
        self.assertIs(self.base_operator.run(), False)

    def test_execution_with_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.base_operator.run()


if __name__ == '__main__':
    unittest.main()