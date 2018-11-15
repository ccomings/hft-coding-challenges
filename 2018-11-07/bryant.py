def threesome(integers):

    if not integers:
        return ['invalid input bro']

    length = len(integers)
    if length < 3:
        return ['not enough ints bro']

    integers.sort()
    result = []
    end = length - 1
    for i in xrange(length - 2):
        a = integers[i]
        start = i + 1
        while start < end:
            b = integers[start]
            c = integers[end]

            if a + b + c == 0:
                result.append((a, b, c))
                start += 1
                end -= 1
            elif a + b + c > 0:
                end -= 1
            else:
                start += 1
    return result
