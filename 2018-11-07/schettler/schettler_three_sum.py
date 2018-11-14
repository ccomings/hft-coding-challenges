#
# Matt Schettler
# Nov 2018
# 
# https://github.com/ccomings/hft-coding-challenges/blob/master/2018-11-07/three_sum.md
# 
import itertools


def main():

    # setup test data
    testdata = [-1, 0, 1, 2, -1, -4]

    # do the work
    results = {str(sorted(x)) for x in itertools.permutations(testdata, 3) if sum(x) == 0}

    # output the results
    print('\n'.join(results))


if __name__ == '__main__':
    main()
