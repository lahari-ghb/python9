#odd
def sum_of_odd_digits(number):
    digits = str(number)
    odd_sum = sum(int(digit) for digit in digits if int(digit) % 2 != 0)
    return odd_sum
number = 1235
result = sum_of_odd_digits(number)
print(f"The sum of odd digits in {number} is {result}")

#armstrong
def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == number
def find_armstrong_numbers(start, end):
    armstrong_numbers = [num for num in range(start, end + 1) if is_armstrong(num)]
    return armstrong_numbers
start_range = 1
end_range = 100
armstrong_numbers = find_armstrong_numbers(start_range, end_range)
print(f"Armstrong numbers between {start_range} and {end_range} are: {armstrong_numbers}")

def smallest_prime_digit(number):
    # List of prime digits (2, 3, 5, 7)
    prime_digits = {2, 3, 5, 7}
    # Convert the number to a string to access each digit
    digits = str(number)
    # Find all prime digits in the number
    primes_in_number = [int(digit) for digit in digits if int(digit) in prime_digits]
    # Return the smallest prime digit if any exist, otherwise return None
    return min(primes_in_number) if primes_in_number else None

#prime
number = 45231
result = smallest_prime_digit(number)
if result is not None:
    print(f"The smallest prime digit in {number} is {result}")
else:
    print(f"There are no prime digits in {number}")
