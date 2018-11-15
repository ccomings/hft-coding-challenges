def three_sum_first_attempt(nums): # first attempt, kinda slow
    problem_length = len(nums)
    if problem_length < 3:
        return []

    solutions = []

    nums.sort()

    start_idx = 0
    middle_idx = 1
    stop_idx = 2

    while start_idx < problem_length - 2:
        while middle_idx < problem_length - 1:
            while stop_idx < problem_length:
                start_number = nums[start_idx]
                middle_number = nums[middle_idx]
                stop_number = nums[stop_idx]

                triplets = [start_number, middle_number, stop_number]
                if start_number + middle_number + stop_number == 0:
                    if triplets not in solutions:
                        solutions.add(triplets)

                stop_idx += 1

            middle_idx += 1
            stop_idx = middle_idx + 1

        start_idx += 1
        middle_idx = start_idx + 1
        stop_idx = middle_idx + 1

    return solutions

def three_sum_second_attempt(nums): # second attempt a lil faster
    problem_length = len(nums)
    if problem_length < 3:
        return []

    num_tracker = set()
    solutions = []

    nums.sort()

    start_idx = 0
    stop_idx = 1

    while start_idx < problem_length - 1:
        while stop_idx < problem_length:
            start_num = nums[start_idx]
            stop_num = nums[stop_idx]

            looking_for_num = 0 - (start_num + stop_num)
            if looking_for_num in num_tracker:
                triplet = [start_num, stop_num, looking_for_num]
                if triplet not in solutions:
                    solutions.append(triplet)

            num_tracker.add(stop_num)
            stop_idx += 1

        start_idx += 1
        stop_idx = start_idx + 1
        num_tracker = set()

    return solutions

# three_sum([-1,0,1,2,-1,-4])
