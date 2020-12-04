#!/usr/bin/env python

"""part1.py: Count number of trees ("#") found in path (input.txt), more info: https://adventofcode.com/2020/day/3"""

current_x_pos = 0
tree_counter = 0

list_of_rows =  [line.rstrip('\n') for line in open("input.txt")]

for row in list_of_rows:
	value_in_row = row[current_x_pos % len(row)]
	if (value_in_row == "#"):
		tree_counter += 1
	current_x_pos += 3

print(f"Total number of trees found: {tree_counter}")