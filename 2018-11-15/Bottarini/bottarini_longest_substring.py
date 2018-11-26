from collections import OrderedDict

def longest_substring(string_to_use):
	result = 0
	dictionary_str = ''.join(OrderedDict.fromkeys(string_to_use))
	print 'Dictionary String: {}'.format(dictionary_str)
	
	result_front = len(dictionary_str)
	substr_front = dictionary_str
	while result_front > 0:
		if substr_front in string_to_use:
			result_front = len(substr_front)
			break
		else:
			substr_front = substr_front[1:]
			
	result_end = len(dictionary_str)
	substr_end = dictionary_str
	while result_end > 0:
		if substr_end in string_to_use:
			result_end = len(substr_end)
			break
		else:
			substr_end = substr_end[:1]
			
	if result_front >= result_end:
		result = result_front
	else:
		result = result_end
	
	return result


def main():
	string_to_use = 'pwwkew'
	longest_substr_count = longest_substring(string_to_use)
	print 'Target {}'.format(string_to_use)
	print 'Result {}'.format(longest_substr_count)


if __name__ == '__main__':
	main()
