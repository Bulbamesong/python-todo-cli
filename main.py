while True:
    question = input("Do you want to see/add/delete the tasks? See/add/delete: ").strip().lower()
    if question == "see":
        file = open("tasks.txt", "r")
        text = file.read()
        print(text)
        file.close()
    elif question == "add":
        file = open("tasks.txt", "a")
        new_task = input("Write a new task: ")
        file.write(f"{new_task}\n")
        file.close()
    elif question == "delete":
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()
        for i, task in enumerate(tasks):
            print(i, task.strip())
        index = int(input("Enter task number: "))
        del tasks[index]
        file = open("tasks.txt", "w")
        for task in tasks:
            file.write(task)
        file.close()
    else:
        print("Invalid operation")