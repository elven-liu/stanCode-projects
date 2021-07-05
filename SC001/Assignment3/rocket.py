"""
File: rocket.py
Name: Elven Liu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
	"""
	This program will draw a rocket including head, belt, upper, lower part. Those elements will
	vary based on the SIZE number.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	The head part are composed with "/" and "\" and it will look like a triangle.
	The first row will have 1 "/\", and the second row will have  "//\\", and so on.
	"""
	for i in range(SIZE):
		# This space is to make sure that the head part will display at the same place with other parts.
		print(" ", end="")
		for j in range(SIZE):
			# to build up the left part which is combined with "/"
			if i+j > SIZE-2:
				print('/', end="")
			else:
				print(" ", end="")
		# to build up the right part which is combined with "\"
		for k in range(i+1):
			print("\\", end="")
		print("")


def belt():
	"""
	The first and the last place will put "+" and the middle part(NUMBER*2) will put "="
	"""
	for i in range( (SIZE + 1) * 2):
		# The first place will put "+"
		if i == 0:
			print('+', end="")
		# Middle places put "="
		elif i < (SIZE + 1) * 2 - 1:
			print('=', end="")
		# Last place will put "+"
		elif i == (SIZE + 1) * 2 - 1:
			print('+', end="")
	print("")


def upper():
	"""
	The first and the last place will put "|". Middle places will put a triangle. The first row is "/\", and the
	second row is "/\""/\", and so on. The other places will put "."

	"""
	for i in range(SIZE):
		for j in range((SIZE+1) * 2):
			# The first and the last place put "|"
			if j == 0 or j == (SIZE+1) * 2 - 1:
				print('|', end="")
			# Set up the rules where we put the "."
			elif i+j < SIZE or j-(i+1) > SIZE:
				print('.', end="")
			# Set up the rules where we put the "/\"
			else:
				# For the scenario that the NUMBER is odd.
				if SIZE % 2 == 1:
					if (i+j) % 2 == 1:
						print('/', end="")
					elif (i+j) % 2 == 0:
						print('\\', end="")
				# For the scenario that the NUMBER is even.
				elif SIZE % 2 == 0:
					if (i+j) % 2 == 1:
						print('\\', end="")
					elif (i+j) % 2 == 0:
						print('/', end="")
		print("")


def lower():
	"""
	The rule of | and . are the same as the upper parts. The middle part in composed with "\""/".
	The first row has NUMBER "\""/", and the second row has NUMBER - 1 "\""/", and so on.
	"""
	for i in range(SIZE):
		for j in range((SIZE+1) * 2):
			# The first and the last place put "|"
			if j == 0 or j == (SIZE+1) * 2 - 1:
				print('|', end="")
			# Set up the rules where we put the "."
			elif j-(i+1) < 0 or i+j > SIZE * 2:
				print('.', end="")
			# Set up the rules where we put the "\"
			elif (i+j) % 2 == 1:
				print('\\', end="")
			# Set up the rules where we put the "/"
			elif (i+j) % 2 == 0:
				print('/', end="")
		print("")

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()