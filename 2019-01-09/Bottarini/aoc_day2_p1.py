# aoc_day2_p1.py
def process_checksum():
	# return_number = 0

	file_name = 'aoc_day2_pt1_input.txt'

	with open(file_name) as file_obj:
		content = file_obj.readlines()

	two_same_chars = []
	three_same_chars = []

	for line in content:
		char_list = []
		for character in line:
			two_exact_found = False
			three_exact_found = False
			if character not in char_list:
				char_count = line.count(character)
				if char_count == 2:
					two_exact_found = True
				elif char_count == 3:
					three_exact_found = True

				if two_exact_found:
					two_same_chars.append(line)
				if three_exact_found:
					three_same_chars.append(line)
				char_list.append(character)
	
	two_same_char_set = set(two_same_chars)
	two_same_char_count = len(two_same_char_set)
	three_same_char_set = set(three_same_chars)
	three_same_char_count = len(three_same_char_set)

	print 'Strings with two exact: {}'.format(two_same_char_set)
	print ''
	print 'Strings with three exact: {}'.format(three_same_char_set)
	print 'Number of two exact: {}'.format(two_same_char_count)
	print 'Number of three exact: {}'.format(three_same_char_count)

	return_number = two_same_char_count * three_same_char_count

	return return_number

def main():
	target = process_checksum()
	print 'Checksum is {}'.format(target)

if __name__ == '__main__':
    main()