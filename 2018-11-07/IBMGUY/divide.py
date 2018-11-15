def divide(dividend, divisor):
    count = 0
    abs_divisor = abs(divisor)
    abs_dividend = abs(dividend)
    running_sum = abs_divisor

    while running_sum <= abs_dividend:
        running_sum += abs_divisor
        count += 1

    if abs_divisor + abs_dividend != abs(divisor + dividend): # check if one value is positive and one is negative
        return count * -1
    else:
        return count
