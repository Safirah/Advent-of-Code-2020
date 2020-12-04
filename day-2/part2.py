#!/usr/bin/env python

"""part2.py: Finds the number of passwords in input.txt that don't follow the rules. Format:
position_1-position_2 letter: password
1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
"""

import re

valid_passwords_count = 0

lines =  [line.rstrip('\n') for line in open("input.txt")]

for line in lines:
	match = re.search("(?P<pos_1>\d+)-(?P<pos_2>\d+) (?P<letter>.): (?P<password>.+)", line)
	pos_1 = int(match.group('pos_1'))
	pos_2 = int(match.group('pos_2'))
	letter = match.group('letter')
	password = match.group('password')

	password_pos_1 = password[pos_1 - 1]
	password_pos_2 = password[pos_2 - 1]

	if (bool(password_pos_1 == letter) is not bool(password_pos_2 == letter)):
		valid_passwords_count = valid_passwords_count + 1

print (f"Valid passwords: {valid_passwords_count}")