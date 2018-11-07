def main():

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

    print "well, it worked!"


if __name__ == '__main__':
    main()