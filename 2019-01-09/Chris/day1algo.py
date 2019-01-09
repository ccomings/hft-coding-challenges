lines = [line.rstrip("\n") for line in open("day1input.txt")]

def counter(array):
    accum = 0
    for num in array:
        accum += int(num)

    print accum

counter(lines)

def fequency_tracker(array):
    dict = {}
    accum = 0
    flag = True

    while flag:
        for num in array:
            if dict.has_key(accum):
                print accum
                flag = False
                break
            else:
                dict[accum] = True
                accum += int(num)

fequency_tracker(lines)
