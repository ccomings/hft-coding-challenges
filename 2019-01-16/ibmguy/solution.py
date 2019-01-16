""" Contains Part 1 Only """

with open('input.txt') as f:
    input = f.readlines()
inputs = [l.strip() for l in input]

def solution():
    repeat_count = 0

    all_coordinates = {}
    for x in range (1000):
        for y in range (1000):
            all_coordinates[(x, y)] = 0

    input_coordinates = parse_input_into_list_of_coordinate_pairs(inputs)
    for coordinate_pair in input_coordinates:
        all_coordinates[coordinate_pair] += 1

    for coordinate_pair, count in all_coordinates.items():
        if count > 0:
            repeat_count += 1

    return repeat_count


def parse_input_into_list_of_coordinate_pairs(inputs):
    all_coordinates = []

    for input in inputs:
        formatted_input = format_input(input)
        start_x, start_y = formatted_input['starting_coordinates']
        spread_x, spread_y = formatted_input['spread']

        for x in range(int(spread_x)):
            for y in range(int(spread_y)):
                all_coordinates.append((x, y))
    return all_coordinates

def format_input(str):
    # regex would probably do this cleaner, but i don't know regex
    inputs_i_care_about = str.split(' ')[2:]
    coordinates = inputs_i_care_about[0].split(',')
    spread = inputs_i_care_about[1].split('x')

    start_x = coordinates[0]
    start_y = coordinates[1].replace(':','')

    spread_x = spread[0]
    spread_y = spread[1]

    return {
        'starting_coordinates': (start_x, start_y),
        'spread': (spread_x, spread_y)
    }


print solution()
