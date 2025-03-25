a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum = a + b
print(f"The sum is: {sum}")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")
