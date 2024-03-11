from f_scheduler.operators.base_op import BaseOperator


class IterFunctionOperator(BaseOperator):
    def __init__(self, function, param, iterations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.function = function
        self.param = param
        self.iterations = iterations
        self.return_value = []

    def execute(self, context: dict) -> bool:
        try:
            for _ in range(self.iterations):
                result = self.function(*self.param)
                if result is not None:
                    self.return_value.append(result)
                else:
                    return True
            return True
        except Exception as e:
            print(f"Function execution failed with error: {e}")
            return False