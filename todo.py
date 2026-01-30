choose_list = [1, 2, 3, 4, 5]
todo_list = {}

def todo(cell, task):
    if cell == 1:
        todo_list[task] = False

    if cell == 2:
        if task in todo_list:
            del todo_list[task]
        else:
            print("\nTask not found.")
            input("Enter to return")

    if cell == 3:
        if not todo_list:
            print("No tasks.")
            input("\nEnter to return")

        else:
            if task in todo_list:
                todo_list[task] = True
            else:
                print("\nTask not found.")
                input("Enter to return")

print("\n[+] Welcome to TODO list!\n\n")

while True:
    print("\n1. Add task\n" \
    "2. Delete task\n" \
    "3. Mark complete\n" \
    "4. Show tasks\n" \
    "5. Quit")

    try:
        choose = int(input("\nChoose Number: "))
    except ValueError:
        print("Please input a number.")
        input("\nEnter to return")
        continue

    if choose not in choose_list:
        continue

    elif choose == 1:
        task = input("Input Add task: ")
        if task in todo_list:
            print("\nTask already exists.")
            input("Enter to return")

        else:
            todo(1, task)

    elif choose == 2:
        task = input("Input Delete task: ")
        todo(2, task)

    elif choose == 3:
        task = input("Input Complete task: ")
        todo(3, task)

    elif choose == 4:
        if not todo_list:
            print("No tasks.")
            input("\nEnter to return")
            continue

        for task, done in todo_list.items():
            mark = "[x]" if done else "[ ]"
            print(f"{mark} {task}")
            continue

    else:
        print("\n\n\n\n[-] See you again!")
        break



