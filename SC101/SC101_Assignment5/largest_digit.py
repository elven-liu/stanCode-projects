"""
File: largest_digit.py
Name: Elven Liu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the numbers to look for the biggest one
	:return: int, the largest number
	"""

	max = 0
	find_largest_digit_helper(n, max)
	return find_largest_digit_helper(n, max)


def find_largest_digit_helper(numbers, current_max):
	if numbers < 0:
		numbers *= (-1)

	if numbers == 0:
		return current_max
	else:
		remainder = numbers % 10
		if remainder > current_max:
			current_max = remainder
		current_max = find_largest_digit_helper((numbers-remainder)//10, current_max)
		return current_max




if __name__ == '__main__':
	main()
