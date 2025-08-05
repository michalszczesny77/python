import math

def rectangle_area(a: int, b: int):
    return a * b

def is_prime(number: int):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_number_in_list(your_list: list):
    output = 0
    for x in your_list:
        output += x
    return output

def number_counter(your_list: list):
    my_dict = {}
    for element in your_list:
        if element in my_dict:
            my_dict[element] += 1
        else:
            my_dict[element] = 1
    return my_dict

numbers = [1, 2, 3, 4, 2, 2, 2, 1]
print(number_counter(numbers))
