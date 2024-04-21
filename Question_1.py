#Task 1 & 2
def add(n1):
    global numbers
    variables = sum(n1)
    print(f"The sum is: {variables}")
    
def subtract(n1, n2):
    global numbers
    for x in numbers:
        minus = numbers[0] - numbers[1]
    print(f"The difference is: {minus}")

def multiply(n1, n2):
    global numbers
    for x in numbers:
        product = numbers[0] * numbers[1]
    print(f"The product is: {product}")

def divide(n1, n2):
    global numbers
    for x in numbers:
        quotient = numbers[0] / numbers[1] #replace these with n1,n2
    print(f"The quotient is: {quotient}")
    

numbers = []

def calculator(): #type error issues
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
            numbers.append(variable1) #why make variables instead of just using variables as arguments
            numbers.append(variable2)
            return add(numbers) #print instead of return for while loops so it doesnt break

        elif choice == "2":
            variable1 = int(input("Input Number 1: "))
            variable2 = int(input("Input Number 2: "))
            numbers.append(variable1)
            numbers.append(variable2)
            return subtract(variable1, variable2)
        elif choice == "3":
            variable1 = int(input("Input Number 1: "))
            variable2 = int(input("Input Number 2: "))
            numbers.append(variable1)
            numbers.append(variable2)
            return multiply(variable1, variable2)
        elif choice == "4":
            variable1 = int(input("Input Number 1: "))
            variable2 = int(input("Input Number 2: "))
            numbers.append(variable1)
            numbers.append(variable2)
            return divide(variable1, variable2)
        else:
            print("Invalid response, please try again")

calculator()