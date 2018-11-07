#!/usr/bin/env python

def myfunc(input):
    # do your main logic for the problem here
    return 1


def main():

    test_data = 'test'

    # run your tests here
    # we expect this function to return 1 for the input 'test'
    assert myfunc(test_data) == 1

    print "well, it worked!"


if __name__ == '__main__':
    main()
