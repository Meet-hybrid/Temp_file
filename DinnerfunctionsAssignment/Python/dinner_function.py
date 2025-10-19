def get_factorial(num):
	int factorial = 1;
	for i in range(1, num + 1):
	factorial = factorial * i
	return factorial

def find_gcd(num_one, num_two):
	gcd = 1
	for i in range(1, min(num_one, num_two) +1)
		if num_one % 1 == 0 and num_two % 1 == 0:
			gcd = i
	return gcd

def find_lcm(num_one, num_two):
	gcd = 1
	for i in range(1, min(num_one, num_two) +1)
		if num_one % 1 == 0 and num_two % 1 == 0:
			gcd = i
	lcm = (num_one * num_two // gcd
	return lcm

def is_perfect_number(number):
	count = 0
	for i in range(1, number):
		if number % i == 0:
			count += i
	return count == number

def is_armstrong(number)
	num_str = str(number)
	num_length = len(num_str)
	count = 0
	for digit in num_str:
		count += int(digit) ** num_length
	if count == number:
		return True
	else:
		return False










