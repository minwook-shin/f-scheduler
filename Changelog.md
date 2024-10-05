# Changelog

## Release 0.4.0

### Features

- add graphlib library to check cycle in the scheduler
  - raise error if cycle is detected

```python
from f_scheduler import DAG

dag = DAG(use_graphlib=True)
```

## Release 0.3.0

### Features

- add repr method to operator classes

## Release 0.2.0

### Features

- add `update_task` method to `DAG` class
  - update task parameters from `Task` instance

## Release 0.1.0

### Features

- add clear, get_return_value, get_all_tasks method to DAG class

## Release 0.0.1

### Features

- First release
    - add operator and module for function scheduling