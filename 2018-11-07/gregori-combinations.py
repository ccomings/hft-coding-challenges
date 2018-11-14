#!/usr/bin/env python
import itertools

def myfunc(lst):
    ret = []
    arr = list(itertools.combinations(lst, 3))

    for (x,y,z) in arr:
        if x+y+z == 0:
            ret.append((x,y,z))

    return ret


def main():
    print myfunc([-1, 0, 1, 2, -1, -4])
    

if __name__ == '__main__':
    main()
