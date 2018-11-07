
def divide_without_division(number, divider):
	count = 0
	scratch_number = abs(number)
	divider = abs(divider)
	is_negative = False

	if (number > 0 and divider < 0) or (number < 0 and divider > 0):
		is_negative = True

	if divider == 0:
		return count
	else:
		while scratch_number > 0:
			scratch_number -= divider
			if scratch_number >= 1:
				count += 1

	print 'Count before negation: {}'.format(count)
	if is_negative:
		count = count - (count + count)

	return count


def main():
	numerator = -5
	divider = 2
	target = divide_without_division(numerator, divider)
	print 'Divide {} by {}'.format(numerator, divider)
	print 'Target is {}'.format(target)

if __name__ == '__main__':
    main()