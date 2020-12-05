#!/usr/bin/env python

"""part1.py: Count number of valid passports in input.txt, more info: https://adventofcode.com/2020/day/4"""
import re

def main():
	with open("input.txt") as f:
		valid_passport_count = 0
		lines = f.read()
		list_of_passports = lines.split("\n\n")

		valid_passports_list = list(filter(lambda passport: is_passport_valid(passport), list_of_passports))
		print (f"There are {len(valid_passports_list)} valid passport(s)")

def is_passport_valid(passport):
	is_byr_valid = re.search("(byr:(19\d{2})|200[0-2])", passport)
	is_iyr_valid = re.search("(iyr:20(1[0-9]|20))", passport)
	is_eyr_valid = re.search("(eyr:20(2[0-9]|30))", passport)
	is_hgt_valid = re.search("(hgt:(((1([5-8]\d)|(19[1-3])))cm)|((59|6\d|7[0-6])in))", passport)
	is_hcl_valid = re.search("(hcl:#[a-f0-9]{6})", passport)
	is_ecl_valid = re.search("(ecl:(amb|blu|brn|gry|grn|hzl|oth))", passport )
	is_pid_valid = re.search("(pid:\d{9})", passport )

	return is_byr_valid and is_iyr_valid and is_eyr_valid and is_hgt_valid and is_hcl_valid and is_ecl_valid and is_pid_valid



if __name__ == "__main__":
	main()