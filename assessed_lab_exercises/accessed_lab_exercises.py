'''
@Author: Riley Jordan
@Date: 20/10/2024
@Version: 1.0
'''

def max_of_three(num1, num2, num3):
    # This function takes three integers as input and returns the maximum of the three given numbers.

    # Initialize the maximum to the first number
    maximum = num1
    # Compare the second and third numbers to the current maximum
    if num2 > maximum:
        maximum = num2
    # Compare the third number to the current maximum
    if num3 > maximum:
        maximum = num3
    # Return the maximum number
    return maximum
'''
maximum = max_of_three(10, 20, 30)
print(maximum, "is the maximum")
'''

def calculator(num1, num2, operator):
    # Inform the user of the available operations they can perform.
    print("Available operations: +, -, /, *, %, >, >=, <, <=")

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        # If the numbers are not integers or floats, the function prints an error message and does not return a result.
        return "Invalid numbers."

    if operator == "/" and num2 == 0:
        # If the second number is 0 and the operator is division, the function prints an error message and does not return a result.
        return "Cannot divide by zero"
    
    # Perform the operation based on the operator provided
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "%":
        result = num1 % num2
    elif operator == ">":
        result = num1 > num2
    elif operator == ">=":
        result = num1 >= num2
    elif operator == "<":
        result = num1 < num2
    elif operator == "<=":
        result = num1 <= num2
    else:
        # If an invalid operator is provided, the function prints an error message and does not return a result.
        return "Invalid operator."
    return result

# Example usage:
## please use 2 numbers and an operator to perform an operation
## operators: +, -, /, *, %, >, >=, <, <=
'''
print(calculator(10, 5, "+"))  # Output: 15
print(calculator(10, 5, "-"))  # Output: 5
print(calculator(10, 5, "/"))  # Output: 2.0
print(calculator(10, 5, "*"))  # Output: 50
print(calculator(10, 5, "%"))  # Output: 0
print(calculator(10, 5, ">"))  # Output: True
print(calculator(10, 5, ">=")) # Output: True
print(calculator(10, 5, "<"))  # Output: False
print(calculator(10, 5, "<=")) # Output: False
print(calculator(10, 0, "/"))  # Output: cannot divide by zero
print(calculator(10, 5, "x"))  # Output: invalid operator
print(calculator("10", 5, "+")) # Output: invalid numbers
'''

def winning_numbers(user_numbers, winning_numbers):
    # makes sure the lists are 3 numbers long
    if len(user_numbers) != 3 or len(winning_numbers) != 3:
        return "Invalid input. Please enter three numbers."

    # Check how many numbers match the winning numbers using set intersection
    # using sets because they are unordered and do not contain duplicates
    ## set() creates a set from the list of numbers
    match_count = len(set(user_numbers) & set(winning_numbers))

    # Determine the prize based on the number of matches
    if match_count == 3:
        prize = "First"
    elif match_count == 2:
        prize = "Second"
    elif match_count == 1:
        prize = "Third"
    else:
        prize = "No"
    # Return the prize won
    print(f"congradulations you have won {prize} prize")
    return prize

# Example usage:
## please use 3 numbers in each list to find if you have won a prize
'''
print(winning_numbers([3, 5, 10], [5, 14, 17]))  # Output: Third
print(winning_numbers([14, 5, 5], [5, 14, 17]))  # Output: Second
print(winning_numbers([5, 14, 17], [5, 14, 17]))  # Output: First
print(winning_numbers([1, 2, 3], [5, 14, 17]))  # Output: No
print(winning_numbers([1, 2], [5, 14, 17]))  # Output: Invalid input. Please enter three numbers.
'''


def sum_of_evens(min_value, max_value):
    # Initialize the total sum to 0
    total = 0
    # Iterate over the range from min_value to max_value (inclusive)
    for i in range(min_value, max_value):
        # checks if number is even
        if i % 2 == 0:
            # add the even number to the total sum
            total += i
    # Print the total sum of even numbers
    # Return the total sum of even numbers
    return total

# example usage:
## please use 2 numbers to find the sum of even numbers between them
'''
min_value = 12
max_value = 21
sum = sum_of_evens(min_value, max_value) 
print(sum)  # Output: 80
'''


def is_prime(num):
    # This function checks if a number is prime.
    # A prime number is a number greater than 1 that has no divisors other than 1 and itself.

    output = True
    # prime numbers are greater than 1
    if num <= 1:
        return not output
    
    # check for factors of the number
    ## int(num**0.5) + 1 == the square root of the number + 1 
    ## this is because the factors of a number are always less than or equal to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return not output
    return output

# # # Run code example
'''
boolean = is_prime(19)   # returns True
print(boolean)
boolean = is_prime(1)   # returns False
print(boolean)
'''

def are_anagrams(str1, str2):
   # This function checks if two strings are anagrams of each other.
    output = True

    # compare the sorted strings lengths
    if len(str1) != len(str2):
        return not output
    
    # compare letters in the strings
    for letter in str1:
        if letter not in str2:
            return not output
    return output

## Example 
'''
print(are_anagrams("listen", "silent"))  # Expected output: True
print(are_anagrams("hello", "world"))    # Expected output: False
'''

def calculate_average(numbers):
    # calculates the average of a list of numbers

    # check if the list is empty
    if len(numbers) == 0:
        average = None
        return average
    
    # calculate the average of the numbers
    total = 0
    for number in numbers:
        total += number
    
    average = total / len(numbers)
    return average

# # Example usage
'''
numbers = [10, 20, 30, 40, 50]
print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0
'''

def calculate_weekly_pay(hours_worked):
    # calculates weekly pay + overtime pay

    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay

    # check if hours_worked is a whole number
    if not isinstance(hours_worked, int):
        # round down to the nearest whole number
        hours_worked = int(hours_worked)

    # check if the hours worked is less than or equal to the standard hours
    if hours_worked <= standard_hours:
        total_pay = hours_worked * regular_rate
    else:
        # calculater regular pay + overtime pay
        regular_pay = standard_hours * regular_rate
        overtime_hours = hours_worked - standard_hours
        overtime_pay = overtime_hours * overtime_rate
        total_pay = regular_pay + overtime_pay
    return total_pay
    
# # Code Example
'''
overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
print(overtime_pay)
'''