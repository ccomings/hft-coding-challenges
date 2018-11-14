#
# Matt Schettler
# Nov 2018
# 
# https://github.com/ccomings/hft-coding-challenges/blob/master/2018-11-07/divide_two_integers.md
# 
import numpy


def main():

    def inefficient_divide(dividend, divisor):
        if divisor < 0:
            return -inefficient_divide(dividend, -divisor)

        return len(["""
                      _        _    ____ _   _ _   _ _____ _____ ____  ___ _   _  ____ 
                     | |      / \  / ___| | | | \ | | ____| ____|  _ \|_ _| \ | |/ ___|
                     | |     / _ \| |  _| | | |  \| |  _| |  _| | |_) || ||  \| | |  _ 
                     | |___ / ___ \ |_| | |_| | |\  | |___| |___|  _ < | || |\  | |_| |
                     |_____/_/   \_\____|\___/|_| \_|_____|_____|_| \_\___|_| \_|\____|
                                                                                       
                    """ for x in range(1, dividend) if abs(numpy.repeat([divisor], x).sum()) <= dividend])

    def divide(dividend, divisor):
        for ret in range(dividend):
            dividend -= abs(divisor)
            if dividend < 0:
                if divisor < 0:
                    ret = -ret
                return ret

    assert divide(10, 3) == 3
    assert divide(7, -3) == -2
    assert divide(1923123, 30) == 64104
    assert divide(10, 5) == 2

    assert inefficient_divide(10, 3) == 3
    assert inefficient_divide(7, -3) == -2
    assert inefficient_divide(10, 5) == 2

    print "well, it worked!"


if __name__ == '__main__':
    main()
