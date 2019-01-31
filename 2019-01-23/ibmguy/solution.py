""" I've got the best
                        _          _   _   _
                      | |        | | | | (_)
 ___ _ __   __ _  __ _| |__   ___| |_| |_ _
/ __| '_ \ / _` |/ _` | '_ \ / _ \ __| __| |
\__ \ |_) | (_| | (_| | | | |  __/ |_| |_| |
|___/ .__/ \__,_|\__, |_| |_|\___|\__|\__|_|
    | |           __/ |
    |_|          |___/
"""
from collections import defaultdict

with open('input.txt') as f:
    input = f.readlines()
inputs = [l.strip() for l in input]
inputs.sort()

def solution_part_one():
    data = parse_input_into_sleeping_minute_map(inputs)

    laziest_guard_id = get_laziest_guard(data)
    minute_where_guard_slept_the_most = get_longest_minute_slept(data[laziest_guard_id])
    sln = laziest_guard_id * minute_where_guard_slept_the_most

    print sln
    return sln

def solution_part_two():
    # make a map of {guard: {longest_minute: ?, minutes_spent: ?}}, use that to get a sln
    guard_to_their_biggest_minute_map = {}

    data = parse_input_into_sleeping_minute_map(inputs)
    for guard, minute_mapping in data.items():
        longest_minute = None
        longest_time_spent_on_minute = 0
        for minute, num_time_spent_asleep_on_dat_minute in minute_mapping.items():
            if num_time_spent_asleep_on_dat_minute > longest_time_spent_on_minute:
                longest_minute = minute
                longest_time_spent_on_minute = num_time_spent_asleep_on_dat_minute

        guard_to_their_biggest_minute_map[guard] = {'longest_minute': longest_minute, 'time_spent_sleepin': longest_time_spent_on_minute}

    laziest_mofo = None
    sleep_record = 0
    sleep_record_minute_for_the_mofo = None

    for guard, laziness_map in guard_to_their_biggest_minute_map.items():
        time_sleepin = laziness_map['time_spent_sleepin']
        if time_sleepin > sleep_record:
            laziest_mofo = guard
            sleep_record = time_sleepin
            sleep_record_minute_for_the_mofo = laziness_map['longest_minute']

    sln = {'guard': laziest_mofo, 'sleepiest_minute': sleep_record_minute_for_the_mofo, 'slept_on_this_minute': sleep_record}
    print sln
    return sln

def get_longest_minute_slept(minute_map_for_guard):
    longest_minute_slept = 0
    most_time_slept_for_guard_per_minute = 0

    for minute_slept_on, num_minutes in minute_map_for_guard.items():
        if num_minutes > most_time_slept_for_guard_per_minute:
            most_time_slept_for_guard_per_minute = num_minutes
            longest_minute_slept = minute_slept_on

    return longest_minute_slept

def get_laziest_guard(data):
    most_minutes_spent_sleepin = 0
    laziest_guard = None

    for guard, minute_map in data.items():
        total_mins_guard_spent_sleeping = sum(minute_map.values())
        if total_mins_guard_spent_sleeping > most_minutes_spent_sleepin:
            most_minutes_spent_sleepin = total_mins_guard_spent_sleeping
            laziest_guard = guard

    return laziest_guard

def parse_input_into_sleeping_minute_map(inputs):
    guard_to_minutes_slept = defaultdict(dict)
    current_guard = 0
    sleep_start = 0
    sleep_end = 0

    for activity in inputs:
        if 'Guard #' in activity:
            # new guard is starting
            current_guard = get_guard_number_from_line(activity)
            if current_guard in guard_to_minutes_slept:
                minutes_slept_map = guard_to_minutes_slept[current_guard]
            else:
                minutes_slept_map = defaultdict(int)
        if 'falls asleep' in activity:
            sleep_start = format_time_from_line(activity)
        if 'wakes up' in activity:
            sleep_end = format_time_from_line(activity)

            for minute in range(sleep_start, sleep_end):
                minutes_slept_map[minute] += 1

            guard_to_minutes_slept[current_guard] = minutes_slept_map

    return guard_to_minutes_slept

def format_time_from_line(line):
    # hr = line[12:14] looks like this isn't needed
    mins = line[15:17]

    return int(mins)

def get_guard_number_from_line(line):
    return int(line.split('Guard #')[1].split(' ')[0])


# solution_part_one()
solution_part_two()
