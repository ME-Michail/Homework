HELP = """
help - напичатать справку по программе.
add - добавить задачу в список (название задачи запрашивается у пользльзователя).
show - напечатать вспе добавленные задачи.
exit - выход из команды"""

tasks =[]

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        print('Задача',task,' добавленна')
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print ("Неизвестная комманда")

