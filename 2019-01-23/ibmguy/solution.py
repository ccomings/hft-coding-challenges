from collections import defaultdict

with open('input.txt') as f:
    input = f.readlines()
inputs = [l.strip() for l in input]

def solution_one():
    inputs.sort()
    data = parse_input_into_sleeping_minute_map(inputs)
    print data

    laziest_guard_id = get_laziest_guard(data)
    minute_where_guard_slept_the_most = get_longest_minute_slept(data[laziest_guard_id])


    sln = laziest_guard_id * minute_where_guard_slept_the_most

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

            print(laziest_guard, most_minutes_spent_sleepin)

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


solution_one()
