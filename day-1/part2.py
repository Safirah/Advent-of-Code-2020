#!/usr/bin/env python

"""part2.py: Finds in the file input.txt 3 numbers that sum up to 2020 and multiplies them"""
from itertools import combinations 

list_of_values =  [int(line.rstrip('\n')) for line in open("input.txt")]

list_of_combinations = combinations(list_of_values, 3)
dict_with_combinations_and_values = dict()

for combination in list_of_combinations:
	if(sum(combination) == 2020):
		combination_value_1 = combination[0]
		combination_value_2 = combination[1]
		combination_value_3 = combination[2]
		print (f"Value 1: {combination_value_1} \nValue 2: {combination_value_2} \nValue 3: {combination_value_3}")
		print (f"Values multiplied: {combination_value_1 * combination_value_2 * combination_value_3}")