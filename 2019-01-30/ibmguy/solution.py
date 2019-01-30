import string

# not complete

with open('input.txt') as f:
    input_list = list(f.readline().strip())

def generate_charset_pair():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase

    reaction_pairs = {}
    for idx, char in enumerate(lowercase_letters):
        uppercase_equivalent = uppercase_letters[idx]
        reaction_pairs[char] = uppercase_equivalent
        reaction_pairs[uppercase_equivalent] = char

    return reaction_pairs

reaction_pairs = generate_charset_pair()

def solution_part_one(input_list):
    dissolved = dissolve(input_list)
    return len(dissolved)

def dissolve(input_list):
    dissolved = False
    # will iterate through the string and 'dissolve' adjacent pairs, 
    # recursively does this until it finds no dissolvable pairs
    for idx, char in enumerate(input_list):
        if idx > 0:
            prev_char = input_list[idx - 1]
            if prev_char == reaction_pairs[char]:
                dissolved = True
                prev_char = input_list[idx - 1]
                input_list.pop(idx - 1)
                input_list.pop(idx - 1)
                idx -= 1

    if dissolved == True:
        return dissolve(input_list)
    else:
        return input_list


print solution_part_one(input_list)
