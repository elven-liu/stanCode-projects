"""
File: quadratic_solver.py
Name:
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Users enter 6 numbers to check if this quadratic equation have solutions.
	"""
	print('stanCode Quadratic solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	discriminant = (b*b) - (4*a*c)

	# make sure discriminant is not < 0
	if discriminant >= 0:
		ans_1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
		ans_2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)

	# print the answers based on different situations(>0, ==0, <0)
	if discriminant > 0:
		print('Two roots:' +str(ans_1) +',' +str(ans_2))
	elif discriminant == 0:
		print('One root:' +str(ans_1))
	else:
		print('No real roots')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
