# if pytest shows an error - you need to install it.
# in the terminal, type the following command:
# pip install pytest
import pytest
from assessed_lab_exercises import (
    calculator,
    max_of_three,
    winning_numbers,
    sum_of_evens,
    are_anagrams,
    is_prime,
    calculate_average,
    calculate_weekly_pay,
    celsius_to_fahrenheit,
    annual_net_income,
    letter_occurrence,
    km_to_miles,
    fuel_cost,
    decrypt_cypher_text,
    is_golden_number,
    find_maximum_difference
)

def test_calculator():
    assert calculator(3, 4, "+") == 7
    assert calculator(10, 5, "-") == 5
    assert calculator(6, 7, "*") == 42
    assert calculator(15, 3, "/") == 5.0
    assert calculator(10, 4, "%") == 2
    assert calculator(5, 3, ">") == True
    assert calculator(5, 5, ">=") == True
    assert calculator(2, 3, "<") == True
    assert calculator(4, 5, "<=") == True
    assert calculator(4, 0, "/") != None
    assert calculator(4, 2, "$/") != None

def test_max_of_three():
    assert max_of_three(10, 20, 30) == 30
    assert max_of_three(5, 15, 10) == 15
    assert max_of_three(7, 7, 7) == 7

def test_winning_numbers():
    assert winning_numbers([1, 2, 3], [1, 2, 3]) == "First"
    assert winning_numbers([1, 2, 4], [1, 2, 3]) == "Second"
    assert winning_numbers([1, 4, 5], [1, 2, 3]) == "Third"
    assert winning_numbers([7, 8, 9], [1, 2, 3]) == "No"

def test_sum_of_evens():
    assert sum_of_evens(1, 10) == 30
    assert sum_of_evens(4, 8) == 18
    assert sum_of_evens(2, 2) == 2
    assert sum_of_evens(2, 3) == 2

def test_are_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("triangle", "integral") == True
    assert are_anagrams("silenn", "siilen") == False


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(1) == False
    assert is_prime(149) == True
    assert is_prime(21) == False
    assert is_prime(63) == False


def test_calculate_average():
    assert calculate_average([10, 20, 30, 40, 50]) == 30.0
    assert calculate_average([5, 10, 15]) == 10.0
    assert calculate_average([7]) == 7.0

def test_calculate_weekly_pay():
    assert calculate_weekly_pay(30) == 360
    assert calculate_weekly_pay(40) == 510
    assert calculate_weekly_pay(50) == 690


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0

def test_annual_net_income():
    assert annual_net_income(50000) == 25000
    assert annual_net_income(35000) == 24500
    assert annual_net_income(25000) == 21250

def test_letter_occurrence():
    assert letter_occurrence("Apple") == 1
    assert letter_occurrence("banana") == 3
    assert letter_occurrence("grape") == 1
    assert letter_occurrence("grapaAa") == 4
    assert letter_occurrence("Hello, World") == 0

def test_km_to_miles():
    assert km_to_miles(100) == 62
    assert km_to_miles(5) == 3.1
    assert km_to_miles(120.453) == 74.681

def test_fuel_cost():
    assert fuel_cost(100) == 13.41
    assert fuel_cost(400) == 53.64
    assert fuel_cost(200) == 26.82

def test_decrypt_cypher_text():
    assert decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$", 3) == "Each error you make in programming is an opportunity to become a better developer!"
    assert decrypt_cypher_text("Hello", 3) == "Ebiil"
    assert decrypt_cypher_text("Hello", 8) == "@]ddg"

def test_find_maximum_difference():
    assert find_maximum_difference([1,5 ,600], [100 ,7, 3 , 602, 39]) == 601
    assert find_maximum_difference( [1,5 ,544], [100 ,7, 3 , 301, 39]) == 541
    assert find_maximum_difference([11,12 ,11, 12, 0], [11 ,11, 11]) == 11
    assert find_maximum_difference([11, 0], [11, 0, 0]) == 11

def test_is_golden_number():
    assert is_golden_number(999) == True
    assert is_golden_number(149) == True
    assert is_golden_number(421) == True
    assert is_golden_number(777) == True
    assert is_golden_number(587) == False
    assert is_golden_number(61) == False
    assert is_golden_number(659) == False

pytest.main()



