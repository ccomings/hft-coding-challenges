import itertools

def main():

    testdata =  [-1, 0, 1, 2, -1, -4]

    results = filter(lambda x: sum(x) == 0, itertools.permutations(testdata, 3))

    print results




if __name__ == '__main__':
    main()
