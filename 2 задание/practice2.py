HELP = """
help - напичатать справку по программе.
add - добавить задачу в список (название задачи запрашивается у пользльзователя).
show - напечатать вспе добавленные задачи.
exit - выход из команды"""

tasks =[]

today =[]
tomorrow =[]
other =[]

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print('Сегодня')
        print(today)
        print('Завтра')
        print(tomorrow)
        print('Другое')
        print(other)
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите название задачи: ")
        if date == "Сегодня":
            today.append(task)

        elif date == "Завтра":
            tomorrow.append(task)
        elif date == "Другое":
            other.append(task)
        print('Задача',task,' добавленна')
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print ("Неизвестная комманда")

