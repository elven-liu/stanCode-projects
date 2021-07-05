"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to quit
EXIT = -1

def main():
	"""
	Users will enter different temperatures and this program will help to find the highest/lowest
	temperature, average temperature and the number of cold days.
	"""
	print('stanCode "Weather Master 4.0"!')
	data = int(input('Next Temperature: (or '+str(EXIT) +' to quit)?' ))
	cold_days = 0
	# count how many cold days
	count_days = 0
	# count how many days in total(for average)
	sum = 0
	# add all temperatures(for average)

	"""
	If users enter EXIT number in the first day, the program will quit directly.
	If users enter temperature, then the program will start calculating based on different situation. 
	"""
	if data == EXIT:
		print('No temperatures were entered')
	else:
		maximum = data
		minimum = data
		count_days += 1
		sum += data
		if data < 16:
			cold_days += 1
		while True:
			data = int(input('Next Temperature: (or '+str(EXIT) +' to quit)?'))
			if data == EXIT:
				break
			if data > maximum:
				# find tha maximum temperature
				maximum = data
			elif data < minimum:
				# find the minimum temperature
				minimum = data
			if data < 16:
				# calculate cold days
				cold_days += 1
			count_days += 1
			sum += data
		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = '+str(minimum))
		print('Average = '+str(sum/count_days))
		print(str(cold_days) +' cold days')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
