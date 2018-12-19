# aoc_day1_p2.py
def add_up_numbers():
	return_number = 0
	x = 0
	frequency_list = []
	puzzle_list = []
	was_found = False

	file_name = 'aoc_day1_p1_input.txt'

	with open(file_name) as file_obj:
		content = file_obj.readlines()

	for line in content:
		puzzle_list.append(int(line.strip()))

	while 1:
		for puzzle_entry in puzzle_list:
			x += puzzle_entry
			if x in frequency_list:
				return_number = x
				was_found = True
				break
			else:
				print '{} was not found!'.format(x)
				frequency_list.append(x)

		if was_found:
			break

	return return_number

def main():
	target = add_up_numbers()
	print 'Target is {}'.format(target)

if __name__ == '__main__':
    main()