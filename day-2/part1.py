#!/usr/bin/env python

"""part1.py: Finds the number of passwords in input.txt that don't follow the rules. Format:
min-max letter: password
1-3 a: abcde  ---> OK
1-3 b: cdefg  ---> NOK"""

import re

valid_passwords_count = 0

lines =  [line.rstrip('\n') for line in open("input.txt")]

for line in lines:
	match = re.search("(?P<min_value>\d+)-(?P<max_value>\d+) (?P<letter>.): (?P<password>.+)", line)
	min_value = int(match.group('min_value'))
	max_value = int(match.group('max_value'))
	letter = match.group('letter')
	password = match.group('password')

	letter_count = password.count(letter)
	if (letter_count >= min_value and letter_count <= max_value):
		valid_passwords_count = valid_passwords_count + 1

print (f"Valid passwords: {valid_passwords_count}")