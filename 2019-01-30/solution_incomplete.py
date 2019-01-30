import string

with open('input.txt') as f:
    input = f.readline().strip()

def solution_part_one(input):

    reaction_pairs = generate_charset_pair()
    input_list = list(input)
    offset = 0

    for idx, char in enumerate(input_list):
        if (idx < 10):
            print (idx, char)
        # print "idx: {}, char: {}".format(idx, char)
        real_index = idx + offset
        if real_index != len(input_list) - 2:
            if char == reaction_pairs[input_list[real_index + 1]]:
                input_list.pop(real_index)
                input_list.pop(real_index)
                offset += -1

    # return ''.join(input_list)

def generate_charset_pair():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase

    reaction_pairs = {}
    for idx, char in enumerate(lowercase_letters):
        uppercase_equivalent = uppercase_letters[idx]
        reaction_pairs[char] = uppercase_equivalent
        reaction_pairs[uppercase_equivalent] = char

    return reaction_pairs

print solution_part_one(input)
