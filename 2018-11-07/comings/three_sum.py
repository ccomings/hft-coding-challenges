from itertools import combinations
import time
import random

class timeitblock(object):

    def __init__(self, name=None):
        self.name = '[{}]'.format(name) if name else 'unnamed timeitblock'

    def __enter__(self):
        self.start = time.time()
        print("{} Starting timed code block...".format(self.name))
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = round(1000.0 * (self.end - self.start), 2)
        print("{} took {} ms.".format(self.name, self.interval))

def three_sum_with_comb(array):
    answer = []
    combs = combinations(array, 3)
    for el in combs:
        if sum(el) == 0:
            answer.append(el)
    return answer

def three_sum(array):
    result = []
    for i in range(0, len(array)-1):
        s = set()
        curr_sum = 0 - array[i]
        for j in range(i+1, len(array)-1):
            if (curr_sum - array[j]) in s:
                result.append([array[i], array[j], curr_sum-array[j]])
            s.add(array[j])
    return result

def main():
    array = [random.randint(-49,49)] * 1000

    with timeitblock("three_sum"):
        three_sum(array)
    with timeitblock("three_sum_with_comb"):
        three_sum_with_comb(array)

if __name__ == '__main__':
    main()
