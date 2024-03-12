from f_scheduler import ConditionOperator, DefaultFunctionOperator, IterFunctionOperator, DAG, Converter


def example_return_func(text):
    return text


dag = DAG()

dag.add_task(DefaultFunctionOperator(function=print, param=(['hello']), task_id='hello_task'))
dag.add_task(DefaultFunctionOperator(function=example_return_func, param=(['bye']), task_id='bye_task'))
dag.add_task(ConditionOperator(10 > 1, task_id='condition_task'))
dag.add_task(IterFunctionOperator(function=example_return_func, param=(['What your name?']), iterations=5, task_id='iter_task'))

task_order = ['hello_task', 'condition_task', 'iter_task', 'bye_task']

# or dag.set_downstream('function_task', 'condition_task')
# dag.set_downstream('condition_task', 'iter_task')
converter = Converter(dag)
converter.convert_list_to_dag(task_order).run('hello_task')

# print return value of iter_task
print(dag.get_return_value('iter_task'))
# print(dag.tasks['iter_task'].return_value)

# print all tasks
print(dag.get_all_tasks())

# clear all tasks
dag.clear()
print(dag.get_all_tasks())
