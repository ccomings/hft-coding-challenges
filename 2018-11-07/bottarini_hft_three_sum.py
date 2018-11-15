def three_sum(list_to_parse):
	result = []
	for i in range(len(list_to_parse)):
	    for j in range(len(list_to_parse)):
	         if i == j:
	             break
	         else:
	             for k in range(len(list_to_parse)):
	                 if k==i or k==j:
	                     break
	                 else:
	                     test_num = (list_to_parse[i] + list_to_parse[j] + list_to_parse[k])
	                     if test_num == 0:
	                         row = [list_to_parse[i], list_to_parse[j], list_to_parse[k]]
	                         row.sort()
	                         if row not in result:
	                             result.append(row)
	
	return result


def main():
	array_to_parse = [-1, 0, 1, 2, -1, -4]
	unique_tuples = three_sum(array_to_parse)
	print 'Target {}'.format(array_to_parse)
	print 'Result is {}'.format(unique_tuples)

if __name__ == '__main__':
    main()
