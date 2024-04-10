#Task 1 & 2
def add():
    global numbers
    variables = sum(numbers)
    print(f"The sum is: {variables}")
    
def subtract():
    global numbers
    for x in numbers:
        minus = numbers[x] - numbers[x+1]

def multiply():
    global numbers
    for x in numbers:
        product = numbers[x] * numbers[x+1]

def divide():
    global numbers
    for x in numbers:
        quotient = numbers[x] / numbers[x+1]
    

numbers = []

def calculator():
    while True:
        print("\n Which arithmetic function would you like to perform?")
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        choice = input("Enter your choice: ")

        if choice == "1":
            variable1 = int(input("Input Number 1: "))
            variable2 = int(input("Input Number 2: "))
            numbers.append(variable1)
            numbers.append(variable2)
            return add(numbers)
            break


