
# coding: utf-8

import itertools

nums = (-1, 0, 1, 2, -1, -4)

combos_list = list(itertools.combinations(nums, 3))

def zero_checker(combos):
    
    sum_zero_combos = []
    
    for comb in combos:
        combo_sum = sum(comb)
        if combo_sum == 0:
            sum_zero_combos.append(comb)
    
    return sum_zero_combos


zero_checker(combos_list)

