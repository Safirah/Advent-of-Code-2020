#!/usr/bin/env python

"""part1.py: Count number of valid passports in input.txt, more info: https://adventofcode.com/2020/day/4"""

def main():
	with open("input.txt") as f:
		valid_passport_count = 0
		lines = f.read()
		list_of_passports = lines.split("\n\n")

		valid_passports_list = list(filter(lambda passport: is_passport_valid(passport), list_of_passports))
		print (f"There are {len(valid_passports_list)} valid passport(s)")

def is_passport_valid(passport):
	return "byr:" in passport and "iyr:" in passport and "eyr:" in passport and "hgt:" in passport and "hcl:" in passport and "ecl:" in passport and "pid:" in passport
	#"cid:" in passport



if __name__ == "__main__":
	main()