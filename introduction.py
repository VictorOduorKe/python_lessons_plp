#display message
print("Welcome to the Python program!")
print("This program will help you learn the basics of Python.")

#display instructions
print("Please follow the instructions carefully.")
print("1. Make sure you have Python installed on your computer.")
print("2. Open your terminal or command prompt.")
print("3. Navigate to the directory where this script is located.")
print("4. Run the script using the command: python introduction.py")    


#functions
def greet_user(name):
    print(f"Hello, {name}", "Welcome to python Pogamming lessons")


#print the message
name = input("Please enter your name: ")
greet_user(name)


#calculator
def add_numbers(num1,num2):
    return num1+num2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = add_numbers(num1, num2)

def substract_numbers(num1,num2):
    return num1 - num2

def multiply_numbers(num1,num2):
    return num1 * num2

def divide_numbers(num1,num2):
    return num1/num2 if num2 !=0 else "Cannot divide by zero"
   

print(f"The sum of {num1} and {num2} is: {result}")
print(f"The difference of {num1} and {num2} is: {substract_numbers(num1, num2)}")
print("The product of {num1} and {num2} is : {multiply_numbers(num1,num2)}")
print(f"The division of {num1} by {num2} is: {divide_numbers(num1,num2)}")