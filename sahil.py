print("Hello, World!")
name = "Alice"
age = 25
height = 5.6
is_student = True

print(name, age, height, is_student)
name = input("Enter your name: ")
print("Hello, " + name + "!")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
p = Person("Alice", 25)
print(p.greet())
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid operator!")
def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)

def show_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
while True:
    choice = input("Choose: add/remove/show/quit: ").lower()
    if choice == "add":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "remove":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "show":
        show_tasks()
    elif choice == "quit":
        break
    else:
        print("Invalid choice!")

