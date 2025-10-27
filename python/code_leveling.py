def append_to_tuple(a, b):
	return a + (5,)
numbers = (1, 2, 3, 4)
print(append_to_tuple(numbers, 5))


def modify_inner_list(tup):
    tup[2][1] = 99
    return tup

numbers = (1, 2, [3, 4], 5)
print( modify_inner_list(numbers))


def add_to_tuple(tup, item):
    temp_list = list(tup)
    temp_list.append(item)
    return tuple(temp_list)
fruits = ('apple', 'banana', 'cherry')
print(add_to_tuple(fruits, 'mango'))


def unpack_tuple(tup):
    a, b, *rest = tup
    return a, b, rest
number = (10, 20, 30, 40)
print(unpack_tuple(number))

from functools import reduce

def get_even_numbers():
	numbers = range(1, 21)
	return list(filter(lambda x: x % 2 == 0,numbers)) 

print(get_even_numbers())

def long_words(words):
    return list(filter(lambda w: len(w) > 5, words))
word = ['cat', 'elephant', 'tiger', 'lion']
print(long_words(word))

def filter_tuples(tuples_list):
    return list(filter(lambda x: x[0] > 2, tuples_list))
list_tuple = [(1, 'A'), (4, 'B'), (2, 'C')]
print(filter_tuples(list_tuple))

def divisible_by_3_and_5():
	numbers = range(1, 51)
	return list(filter(lambda x: x % 3 == 0 and x % 5 == 0, number))

print(divisible_by_3_and_5())

def get_palindromes(words):
    return list(filter(lambda w: w == w[::-1], words))
words = ['level', 'world', 'madam', 'python']
print(get_palindromes(words))






