from itertools import combinations

def three_sum(array):
    answer = []
    combs = combinations(array, 3)
    for el in combs:
        if sum(el) == 0:
            answer.append(el)

    return answer

def main():
    print three_sum([-1, 0, 1, 2, -1, -3])

if __name__ == '__main__':
    main()
