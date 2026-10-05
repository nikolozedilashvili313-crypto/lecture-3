def add_task_fixed(task_name, task_list=None):
    if task_list is None:
        task_list = []  
    task_list.append(task_name)
    return task_list

print(add_task_fixed("დავალება 1")) 
print(add_task_fixed("დავალება 2"))  
print(add_task_fixed("დავალება 3"))