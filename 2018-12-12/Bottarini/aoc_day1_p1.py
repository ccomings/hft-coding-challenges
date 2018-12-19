# aoc_day1_p1.py
def add_up_numbers():
	return_number = 0

	file_name = 'aoc_day1_p1_input.txt'

	with open(file_name) as file_obj:
		content = file_obj.readlines()

	for line in content:
		x = int(line.strip())
		return_number += x

	return return_number

def main():
	target = add_up_numbers()
	print 'Target is {}'.format(target)

if __name__ == '__main__':
    main()