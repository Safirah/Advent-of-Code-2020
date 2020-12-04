#!/usr/bin/env python

"""part2.py: Count number of trees ("#") found in path (input.txt), more info: https://adventofcode.com/2020/day/3"""

list_of_rows =  [line.rstrip('\n') for line in open("input.txt")]

def main():
	total_tree_counter = tree_counter({"x" : 1, "y" : 1})
	total_tree_counter *= tree_counter({"x" : 3, "y" : 1})
	total_tree_counter *= tree_counter({"x" : 5, "y" : 1})
	total_tree_counter *= tree_counter({"x" : 7, "y" : 1})
	total_tree_counter *= tree_counter({"x" : 1, "y" : 2})

	print(f"Total number of trees found: {total_tree_counter}")

def tree_counter(slope):
	current_x_pos = 0
	tree_counter = 0
	for row in list_of_rows[0 : len(list_of_rows) : slope["y"]]:
		value_in_row = row[current_x_pos % len(row)]
		if (value_in_row == "#"):
			tree_counter += 1
		current_x_pos += slope["x"]

	print(f"Total number of trees found on slope ({slope}): {tree_counter}")
	return tree_counter

if __name__ == "__main__":
    main()