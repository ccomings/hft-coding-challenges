def create_search_dict(board):
	search_dict = dict()
	row_pos = 0
	for row in board:
		col_pos = 0
		for col in row:
			tuple_str = '({},{})'.format(row_pos, col_pos)
			dict_value = row[col_pos]
			search_dict.update({tuple_str: dict_value})
			col_pos += 1
		row_pos += 1
	return search_dict
			
def get_search_keys_for_letter(search_dict, search_letter):
	list_to_return = [i for i,j in search_dict.items() if j == search_letter]
	return list_to_return
	
def are_points_adjacent(point1, point2):
	result = False
	if point1 != point2:
		x_diff = abs(point2[0] - point1[0])
		y_diff = abs(point2[1] - point1[1])
		
		if x_diff == 1 and y_diff == 0:
			result = True
		elif y_diff == 1 and x_diff == 0:
			result = True
		
	return result

def word_search(search_dict, string_to_use, print_links=False):
	from ast import literal_eval
	result = False
	search_results_list = []
	used_tuple_list = []
	list_from_string = list(string_to_use)
	word_length = len(list_from_string)
	if word_length == 0:
		pass
	elif word_length == 1:
		single_letter = list_from_string[0]
		start_tuple_str_list = get_search_keys_for_letter(search_dict, single_letter)
		if start_tuple_str_list:
			result = True
	else:
		for i in range(0, word_length):
			current_letter = list_from_string[i]
			start_tuple_str_list = get_search_keys_for_letter(search_dict, current_letter)
			try:
				next_letter = list_from_string[i + 1]
				next_tuple_str_list = get_search_keys_for_letter(search_dict, next_letter)
				is_link_found = False
				for start_tuple_str in start_tuple_str_list:
					if is_link_found:
						break
					start_tuple = literal_eval(start_tuple_str)
					if start_tuple not in used_tuple_list:
						for next_tuple_str in next_tuple_str_list:
							next_tuple = literal_eval(next_tuple_str)
							if next_tuple not in used_tuple_list:
								adj_test = are_points_adjacent(start_tuple, next_tuple)
								if adj_test:
									is_link_found = True
									if print_links:
										print 'Link found with Tuples {} and {}'.format(start_tuple, next_tuple)
									used_tuple_list.append(start_tuple)
				search_results_list.append(is_link_found)
			except IndexError:
				pass
				
	result = all(search_results_list)
	
	return result


def main():
	board_to_use = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]
	target_dict = create_search_dict(board_to_use)
	print 'Board {}'.format(board_to_use)
	
	word_search_str = 'ABCCED'
	print 'Target {}'.format(word_search_str)
	is_word_there = word_search(target_dict, word_search_str, True)
	print 'Result {}'.format(is_word_there)
	
	word_search_str = 'SEE'
	print 'Target {}'.format(word_search_str)
	is_word_there = word_search(target_dict, word_search_str)
	print 'Result {}'.format(is_word_there)

	word_search_str = 'ABCB'
	print 'Target {}'.format(word_search_str)
	is_word_there = word_search(target_dict, word_search_str)
	print 'Result {}'.format(is_word_there)


if __name__ == '__main__':
	main()
