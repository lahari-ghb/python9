# Input: 
# ● Enter your name: Alice   
# ● Enter your age: 25 
# Expected output:   
# ● The data type of name is: <class 'str'>   
# ● The data type of age is: <class 'int'> 

name=(input("enter your name:"))
age=int(input("enter your age:"))
print(type(name))
print(type(age))

#write a code to print Prime numbers between the range.

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
print("Prime numbers between {a} and {b} are:")
for num in range(a,b+ 1):
    if num > 1:  # Check if the number is greater than 1
        for i in range(2, num):  # Check divisibility
            if num % i == 0:
                break
        else:  # Execute if the loop doesn't break (it's a prime number)
            print(num, end=" ")
        
# Write a program that checks if numbers in the range -10 to 260 are interned by python 

for num in range(-10, 261):  
    a = num   
    b = num  
    if a is b:  # Check if the two variables refer to the same memory location
        # print(f"{num} is interned by Python")
        print(f"{num} is true")
    else:
        print(f"{num} is false")

# 2. Write a Python program that: 
# ● Takes two numbers as input 
# ● Asks the user for an operation (+, -, *, /, //, %, **) 
# ● Performs the operation and prints the result

a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
# Ask the user for an operation
op= input("Enter the operation (+,-,*,/,//,%,**): ")
# Perform the operations
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b if b != 0 else "Error: Division by zero"
elif op == "//":
    result = a // b if b != 0 else "Error: Division by zero"
elif op == "%":
    result = a % b if b != 0 else "Error: Division by zero"
elif op == "**":
    result = a ** b
else:
   result = "Error: Invalid operation"
print("Result:", result)

# Write a program to check Leap Year.

year = int(input("Enter a year: "))
# Check leap year conditions
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Write a program to print the sum of the digits of a given number.
num= input("Enter a number: ")
sum= 0  
for digit in num:
    sum += int(digit)  # Convert each character to an integer and add to the sum
print("The sum of the digits is:", sum)
