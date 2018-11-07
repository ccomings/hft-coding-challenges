def main():

    def divide(dividend, divisor):
        ret = 0
        while 1:
            dividend -= abs(divisor)
            if dividend < 0:
                if divisor < 0:
                    ret = -ret
                return ret
            ret += 1

    print divide(10, 3)
    print divide(7, -3)

if __name__ == '__main__':
    main()
