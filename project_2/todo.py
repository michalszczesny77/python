class Task:

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def display(self, i):
        print(f"{i}. {self.priority}:{self.name}")


class CyclicTask(Task):

    def __init__(self, name, priority, frequency):
        super().__init__(name, priority)
        self.frequency = frequency

    def display(self, i):
        print(f"{i}. {self.priority}:{self.name} ({self.frequency})")


class TaskManager:

    def __init__(self):
        self.tasks = []

    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r") as rf:
                for line in rf:
                    module = line.strip().split("|")
                    if len(module) == 3:
                        priority, name, frequency = module
                        self.tasks.append(CyclicTask(name, priority, frequency))
                    elif len(module) == 2:
                        priority, name  = module
                        self.tasks.append(Task(name, priority))
                    else:
                        continue

        except FileNotFoundError:
            pass

    def show_tasks(self):
        if not self.tasks:
            print("You have no tasks!")
        else:
            print("\nYour tasks: ")
            for i, task in enumerate(self.tasks, start=1):
                task.display(i)

    def update_tasks(self):
        with open("tasks.txt", "w") as wf:
            for task in self.tasks:
                if isinstance(task, CyclicTask):
                    wf.write(f"{task.priority.upper()}|{task.name}|{task.frequency}\n")
                else:
                    wf.write(f"{task.priority.upper()}|{task.name}\n")

    def choose_type_of_task(self, name, priority):
        while True:
            task_type = input("Enter type of task - normal (n) or frequent (f): ")

            if task_type.lower() == "n":
                new_task = Task(name, priority)
                self.tasks.append(new_task)
                break

            elif task_type.lower() == "f":
                frequency = str(input("Enter frequency of your task: ")).strip()
                while frequency == "":
                    print("Enter frequency!")
                    frequency = str(input("Enter frequency of your task: "))
                new_task = CyclicTask(name, priority, frequency)
                self.tasks.append(new_task)
                break

            else:
                print("Enter a correct value!")

        self.update_tasks()

    def task_priority(self, name):
        while True:
            task_priority = input("Enter task priority (l)->low, (m)->medium, (h)->high: ")

            if task_priority == "":
                priority = "M"
                break
            if task_priority.lower() == "m":
                priority = "M"
                break
            elif task_priority.lower() == "l":
                priority = "L"
                break
            elif task_priority.lower() == "h":
                priority = "H"
                break
            else:
                print("Invalid value!")

        self.choose_type_of_task(name, priority)

    def remove_task(self):
        if not self.tasks:
            print("You have nothing to remove from the list!")
        else:
            while True:
                try:
                    self.show_tasks()
                    command = input("Enter a number of task to remove or type 'menu' to cancel: ")
                    if command.lower() == 'menu':
                        break
                    number_to_remove = int(command)
                    if number_to_remove < 1:
                        print("Invalid Value! Enter a correct number.")
                    else:
                        number_of_removed_task = number_to_remove - 1
                        removed_task = self.tasks.pop(number_of_removed_task)
                        print(f"{removed_task.name.upper()} task has been removed from the list!")
                        self.update_tasks()
                        break
                except (IndexError, ValueError):
                    print("Invalid Value! Enter a correct number.")

    def filter_by_priority(self):

        priority = input("Enter priority (L/M/H): ").upper()
        exists = False
        for i, task in enumerate(self.tasks, start=1):
            if task.priority.upper() == priority:
                task.display(i)
                exists = True
        if not exists:
            print("You don't have tasks with that priority!")

    def app_start(self):
        self.load_tasks_from_file()
        while True:
            try:
                print("""
Task Manager
1. Add task
2. Show tasks 
3. Remove task
4. Filter by priority
5. Exit
""")
                option = int(input("Enter your choice: "))
                if option == 1:
                    name = input("Enter task name or type 'menu' to quit: ")
                    while name == "":
                        print("You didn't enter text!")
                        name = input("Enter task name or type 'menu' to quit: ")
                    if name.lower() != "menu":
                        self.task_priority(name)
                elif option == 2:
                    self.show_tasks()
                elif option == 3:
                    self.remove_task()
                elif option == 4:
                    self.filter_by_priority()
                elif option == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid number!")
            except ValueError:
                print("Invalid Value!")



test = TaskManager()
test.app_start()