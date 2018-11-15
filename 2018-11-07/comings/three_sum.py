from itertools import combinations

# def three_sum(array):
#     answer = []
#     combs = combinations(array, 3)
#     for el in combs:
#         if sum(el) == 0:
#             answer.append(el)
#
#     return answer

def three_sum(array):
    result = []
    for i in range(0, len(array)-1):
        s = set()
        curr_sum = 0 - array[i]
        for j in range(i+1, len(array)):
            if (curr_sum - array[j]) in s:
                print("Triplet is" + " " + str(array[i]) + " "
                         + str(array[j]) + " " + str(curr_sum-array[j]))
                result.append([array[i], array[j], curr_sum-array[j]])
            s.add(array[j])
    return result

def main():
    print three_sum([-1, 0, 1, 2, -1, -3])

if __name__ == '__main__':
    main()
