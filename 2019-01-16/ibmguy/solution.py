""" Contains Part 1 Only """

from collections import defaultdict

with open('input.txt') as f:
    input = f.readlines()
inputs = [l.strip() for l in input]

def solution_part_1():
    repeat_count = 0
    coordinate_counter = create_coordinate_counter_dict()['counter_dict']

    for coordinate_pair, count in coordinate_counter.items():
        if count > 1:
            repeat_count += 1

    return repeat_count

def solution_part_2():
    coordinate_data = create_coordinate_counter_dict()
    coordinate_counter = coordinate_data['counter_dict']
    input_data = coordinate_data['input_data']
    ids = input_data['ids']
    coordinates = input_data['coordinates']

    for idx in range(len(ids)):
        coordinates_for_claim_id = coordinates[idx]
        claim_counts_for_coordinates = [coordinate_counter[coordinate] for coordinate in coordinates_for_claim_id]
        if claim_counts_for_coordinates == [1]*len(claim_counts_for_coordinates):
            return ids[idx]


def create_coordinate_counter_dict(): # returns a defaultdict mapping coordinates to their count of claims
    coordinate_counter = defaultdict(int)

    parsed_input_data = parse_input_into_list_of_coordinate_pairs(inputs)
    input_coordinates = parsed_input_data['coordinates']

    # flatten list of coordinates (unflattened is used for question 2)
    flattened_coordinates = [coordinate for coordinate_list in input_coordinates for coordinate in coordinate_list]

    for coordinate_pair in flattened_coordinates:
        coordinate_counter[coordinate_pair] += 1

    return {"counter_dict": coordinate_counter, "input_data": parsed_input_data}

def parse_input_into_list_of_coordinate_pairs(inputs):
    all_coordinates = []
    all_ids = []

    for input in inputs:
        formatted_input = format_input(input)
        start_x, start_y = [int(n) for n in formatted_input['starting_coordinates']]
        spread_x, spread_y = [int(n) for n in formatted_input['spread']]

        coordinate_group = []

        for x in range(spread_x):
            for y in range(spread_y):
                coordinate_group.append((start_x + x, start_y + y))

        all_ids.append(formatted_input['id'])
        all_coordinates.append(coordinate_group)


    return {'ids': all_ids, 'coordinates': all_coordinates}

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
        'spread': (spread_x, spread_y),
        'id': str.split(' ')[0],
    }


print solution_part_2()
