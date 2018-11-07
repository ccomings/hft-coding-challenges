import itertools


def main():

    testdata =  [-1, 0, 1, 2, -1, -4]

    results = {str(sorted(x)) for x in itertools.permutations(testdata, 3) if sum(x) == 0}

    print(results)


if __name__ == '__main__':
    main()

