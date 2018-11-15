def divide(dividend, divisor):
    num = 0
    cur_num = dividend
    is_neg = False
    if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
        is_neg = True
    cur_num = abs(dividend)
    divisor = abs(divisor)
    while cur_num >= divisor:
        cur_num -= divisor
        num += 1
    if is_neg == True:
        return num * -1
    else:
        return num

def main():
    print divide(4,3)
    print divide(2,-1)
    print divide(16,4)

if __name__ == '__main__':
    main()
