import itertools

def main():

    testdata =  [-1, 0, 1, 2, -1, -4]

    for perm in itertools.permutations(testdata, 3):
        if sum(perm) == 0:
            print perm



if __name__ == '__main__':
    main()
