def max_of_three(num1, num2, num3):
    # takes three integers as input and returns the maximum of the three given numbers.

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

def calculator(num1, num2, operator):
    # calculates using two numbers and an operator

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

def winning_numbers(user_list, winning_list):
    # checks if user has won a prize if number matches

    # makes sure the lists are 3 numbers long
    if len(user_list) != 3 or len(winning_list) != 3:
        return "Invalid input. Please enter three numbers."

    # Check how many numbers match the winning numbers using set intersection
    ## set() creates a set from the list of numbers
    match_count = len(set(user_list) & set(winning_list))

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
    return prize

def sum_of_evens(min_value, max_value):
    # calculates the sum of even numbers between two numbers

    # Initialize the total sum to 0
    total = 0
    # Iterate over the range from min_value to max_value (inclusive)
    for i in range(min_value -1, max_value + 1):
        # checks if number is even
        if i % 2 == 0:
            # add the even number to the total sum
            total += i
    # Print the total sum of even numbers
    # Return the total sum of even numbers
    return total

def is_prime(num):
    # checks if a number is prime.

    # Initialize the output to True
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

def are_anagrams(str1, str2):
   # Checks if two strings are anagrams of each other.

   # initialize the output to true
    output = True

    # compare the sorted strings lengths
    if len(str1) != len(str2):
        # if the lengths are not equal, the strings are not anagrams
        return not output
    
    # compare the sorted versions of the strings
    if sorted(str1) != sorted(str2):
        return not output
    # if the strings are anagrams, return True
    return output

def calculate_average(numbers):
    # calculates the average of a list of numbers

    # check if the list is empty
    if len(numbers) == 0:
        average = None
        return average
    
    # calculate the average of the numbers
    ## sum of numbers divided by the number of numbers
    total = 0
    for number in numbers:
        # add the number to the total
        total = total + number
    
    average = total / len(numbers)
    return average

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
    
def km_to_miles(kilometers):
    # converts kilometers to miles

    # if negative kilometers, make it positive
    kilometers = abs(kilometers)

    # 1 kilometer is equal to 0.62 miles (round to nearest 3)
    miles = round(kilometers * 0.62, 3)
    # return the distance in miles
    return miles

def celsius_to_fahrenheit(celsius):
   # converts celsius to fahrenheit

   # formula to convert celsius to fahrenheit
   output = (celsius * 9/5) + 32
   # return the temperature in fahrenheit
   return output

def annual_net_income(gross_salary):
    # calculates the net income after tax deductions

    # checks if the gross salary is less than 30,000
    if gross_salary < 30000:
        tax = 0.15
    # checks if the gross salary is between 30,000 and 45,000
    elif 30000 <= gross_salary < 45000:
        tax = 0.30
    # checks if the gross salary is greater than 45,000
    elif gross_salary >= 45000:
        tax = 0.50
    # calculates the net salary after tax deductions
    net_salary = gross_salary - (gross_salary * tax)
    # rounds the net salary to 2 decimal places (incase of float)
    net_salary = round(net_salary, 2)
    return net_salary

def letter_occurrence(input_string):
    # shows the number of a or A in a string

    # counts number of a or A in a string
    count = 0
    # iterate over the string
    for letter in input_string:
        # checks if letters are "a" or "A"
        if letter == "a" or letter == "A":
            # increment the count
            count = count + 1
    # return the count of "a" or "A" in the string
    return count

def fuel_cost(distance_miles):#
    # calculates the cost of fuel for a distance travelled

    # makes distance_miles a float and only positive
    distance_miles = abs(float(distance_miles))

    # Constants
    MPG = 50 # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter

    # calculate total cost of fuel
    total_cost = (distance_miles / MPG) * LITERS_PER_GALLON * PRICE_PER_LITER
    return total_cost

def find_maximum_difference(a, b):
    # Maximm difference between any two elements in two lists

    # Initialize the maximum difference to 0
    maximum = 0
    # iterates through two list max() to find the maximum difference
    ## max() returns the largest number
    for i in a:
        # iterates through the second list
        for j in b:
            maximum = max(maximum, abs(i-j))
    return maximum

def is_golden_number(n):
    # conditions: a + b = n and a * b is divisible by 1000

    # Initialize the boolean to False
    boolean = False
    # check if n is positive
    if n >= 0:
        # iterate through all possible values of a and b up to n
        for a in range(1, n):
            b = n - a
            # check if the conditions are met
            if a * b % 1000 == 0:
                # if the conditions are met, return True
                return not boolean
        # if the conditions are not met, return False
    return boolean
    
def decrypt_cypher_text(encrypted_text, key):
    # decypt the text using the key

    # Initialize the decrypted text to an empty string
    decrypted_text = ""
    # iterates through every character in the encrypted text
    for i in encrypted_text:
        # decrypts the character and adds it to the decrypted text
        decrypted_text = decrypted_text + chr((ord(i) - key) % 256)
    return decrypted_text
