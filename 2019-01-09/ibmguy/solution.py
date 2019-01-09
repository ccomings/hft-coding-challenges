from collections import defaultdict

with open('input.txt') as f:
    input = f.readlines()
input = [l.strip() for l in input]

def convert_string_to_letter_count_dicts(str):
    letter_count_dict = defaultdict(int)

    for char in str:
        letter_count_dict[char] += 1

    return letter_count_dict

def solution_one(input_array):
    two_char_repeat_count = 0
    three_char_repeat_count = 0

    for str in input_array:
        count_dict = convert_string_to_letter_count_dicts(str)

        found_three_unique = False
        found_two_unique = False

        for char, count in count_dict.items():
            if count == 2:
                if found_two_unique == False:
                    two_char_repeat_count += 1
                    found_two_unique = True
            elif count == 3:
                if found_three_unique == False:
                    three_char_repeat_count += 1
                    found_three_unique = True

    return two_char_repeat_count * three_char_repeat_count

def solution_two(input_array):
    str_candidates = set()

    for str in input_array:
        for char_idx in range(0, len(str)):
            snipped_str = str[:char_idx] + str[char_idx + 1:]

            if snipped_str != '':
                if snipped_str in str_candidates:
                    return snipped_str
                else:
                    str_candidates.add(snipped_str)
