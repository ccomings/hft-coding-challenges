#!/usr/bin/python

def myfunc(dividend,divisor):
	count = 0
	is_neg = False
	
	# determine answer sign
	if dividend < 0 or divisor < 0:
		if not (dividend < 0 and divisor < 0):
			is_neg = True
		dividend = abs(dividend)
		divisor = abs(divisor)
			
	# do division
	while dividend >= divisor:
		dividend -= divisor
		count += 1

	return 0 - count if is_neg else count


def main():
	print "DivThis!(4, 2) = {}".format(myfunc(4, 2))


if __name__ == '__main__':
	main()