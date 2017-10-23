print ("Welcome to my TODO program.")
to_do_tasks = []
done_task = []

tasks = []

while True:

    action = raw_input('Select add new task or edit existing tasks (new/edit)')
    if action == 'new':
        task_name = raw_input("Please enter new task: ")
        task = {
            'task_name': task_name,
            'task_done': False
        }
        print("Your task is: {0}".format(task))
        to_do_tasks.append(task)

    elif action == 'edit':

        task_to_edit = raw_input("Enter task name to mark as done: ")

        for task in to_do_tasks:#namesto postavke "task" karkoli, ni nujno da je beseda task
            if task['task_name'] == task_to_edit:
                to_do_tasks.remove(task)
                task['task_done'] = True
                done_task.append(task)
    elif action == 'finish':
        break

#shranimo v en file
with open('todo.csv', 'w+') as todo_file:
    todo_file.writelines('Task Name, Tasl Done\n')
    for task in to_do_tasks:
        todo_file.writelines('{task_name},{task_done}\n'.format(
            task_name=task ['task_name'],
            task_done=task['task_done']
            )
        )


print("Done tasks: {0}".format(done_task))
print("TODO tasks: {0}".format(to_do_tasks))
print ("END")




# empty_list = []
# print(empty_list)
# print(type(empty_list))
#
# list_with_el = [0, '1', "124abc", 2.1, True]
# print(list_with_el)
# print(type(list_with_el))
#
# x = 'neki'
# y = 'neki druzga'
#
# list_xy = [x, y]
# print(list_xy)
# print(type(list_xy))
