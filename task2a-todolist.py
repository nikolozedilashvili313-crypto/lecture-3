#task-A
def add_task(task_name, task_list=[]):
    task_list.append(task_name)
    return task_list


print(add_task("დავალება 1"))  
print(add_task("დავალება 2"))
print(add_task("დავალება 3"))

#ეს სია შეიქმნა მხოლოდ ერთხელ(როცა კოდი ჩაირთო)და ყოველ გამოძახებაზე ახალს კი არ ქმნის, არამედ იმავე ძველ სიას იყენებს.
#ამიტომაც ყველა დავალება ერთ სიაში ხვდება.