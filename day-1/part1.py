#!/usr/bin/env python

"""part1.py: Finds in the file input.txt 2 numbers that sum up to 2020 and multiplies them"""

list_of_values =  [int(line.rstrip('\n')) for line in open("input.txt")]

for file_value in list_of_values:
	expected_pair = 2020 - file_value
	list_of_values_without_current_value = list_of_values.copy()
	list_of_values_without_current_value.remove(file_value)
	if expected_pair in list_of_values_without_current_value:
		print (f"Pair 1: {file_value} \nPair 2: {expected_pair}")
		print (f"Values multiplied: {file_value * expected_pair}")
		break

#Note: This code could be improved if I found a way to not duplicate the list, I'm using the variable list_of_values_without_current_value, because if there was a singular "1010" in the file, then it would count as a pair.