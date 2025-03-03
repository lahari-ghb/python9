# Function to calculate factorial
def calculate_factorial(number):
    # Initialize factorial as 1
    factorial = 1
    # Initialize a counter variable
    counter = number
    
    # Use a while loop to multiply the numbers
    while counter > 1:
        factorial *= counter
        counter -= 1
    
    return factorial

# Get the number from the user
number = int(input("Enter a number: "))

# Call the function and print the result
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")



def print_multiplication_table(number):
    for i in range(1, 21):
        result = number * i
        print(f"{number} x {i} = {result}")
number = int(input("Enter a number: "))
print_multiplication_table(number)


for i in range(1, 101):
    # Check if the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print(i)

