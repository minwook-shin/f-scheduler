import unittest
from unittest.mock import Mock
from f_scheduler.operators.function_op import DefaultFunctionOperator


class TestDefaultFunctionOperator(unittest.TestCase):
    def setUp(self):
        self.mock_function = Mock()
        self.operator = DefaultFunctionOperator(self.mock_function, (1, 2), task_id='task_id')

    def test_function_execution_returns_value(self):
        self.mock_function.return_value = 'value'
        self.assertEqual(self.operator.execute({}), 'value')

    def test_function_execution_returns_none(self):
        self.mock_function.return_value = None
        self.assertFalse(self.operator.execute({}))


if __name__ == '__main__':
    unittest.main()
