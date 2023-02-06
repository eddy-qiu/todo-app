import functions
import time

print("It is " + time.strftime("%b %d, %Y %H:%M:%S"))
while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.startswith('add'):

        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1}-{item}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()
            todos[number - 1] = input("Enter a new todo:") + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command was not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            removed_todo = todos.pop(number - 1).strip('\n')
            functions.write_todos(todos)
            print(f'Todo {removed_todo} was removed from the list.')
        except ValueError:
            print('Your command was not valid.')
            continue

    elif user_action.startswith('exit'):
        break
