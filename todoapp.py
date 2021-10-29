import datetime


todo = {}
DRAFT = "Draft"
IN_PROGRESS = "In Progress"
COMPLETED = "Completed"
DATE_FORMAT = "%Y-%M-%d %H:%M:%S"


def create_todo():
    user_input = str(input("Enter Todo: "))
    if user_input in todo.keys():
        print("Todo already exists.")
        return
    todo.update({
        user_input: {
            "status": DRAFT,
            "start": None,
            "end": None
        }
    })
    print("Successfully created todo.")
    return


def delete_todo():
    if not todo:
            print("No Todo found.")
            return
    
    user_input = str(input("Enter todo tile to be deleted: "))
    if user_input not in todo.keys():
        print("Not found.")
        return
    
    if todo[user_input]["status"] != DRAFT:
        print("Only draft status can be deleted.")
        return
    
    todo.pop(user_input)
    print("Successfully deleted todo.")
    return    input_mapper()[user_input]()



def search_todo():
    user_input = str(input("Enter todo to search: "))
    if user_input in todo.keys():
        print(todo[user_input])
        return
    
    print("No result found.")
    return


def start_todo():
    user_input = str(input("Enter todo to start: "))
    if user_input not in todo.keys():
        print("No todo to start.")
        return
    
    todo[user_input]["status"] = IN_PROGRESS
    todo[user_input]["start"] = datetime.datetime.now().strftime(DATE_FORMAT)
    print(f"{user_input} started successfully.")


def complete_todo():
    user_input = str(input("Enter todo to complete: "))
    if user_input not in todo.keys():
        print("No todo to complete.")
        return
    
    todo[user_input]["status"] = COMPLETED
    todo[user_input]["end"] = datetime.datetime.now().strftime(DATE_FORMAT)
    print(f"{user_input} completed successfully.")


def display_todo():
    if not todo:
        print("No Todo list found.")
        return
    
    print(todo)
    return


def input_mapper():
    return {
        1: create_todo,
        2: delete_todo,
        3: start_todo,
        4: complete_todo,
        5: search_todo,
        6: display_todo
    }


def todo_app(user_input):
    input_mapper()[user_input]()


while True:
    try:
        user_input = int(input("Welcome to ToDo App \nHere are list of commands: \n1.Create \n2.Delete \n3.Start \n4.Complete \n5.Search \n6.Display \n"))
    except ValueError:
        print("Invalid input")
        break
    if user_input == 7:
        break

    todo_app(user_input)
