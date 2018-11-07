def main():

    def divide(dividend, divisor):
        for ret in range(dividend):
            dividend -= abs(divisor)
            if dividend < 0:
                if divisor < 0:
                    ret = -ret
                return ret
            ret += 1

    assert divide(10, 3) == 3
    assert divide(7, -3) == -2


if __name__ == '__main__':
    main()
