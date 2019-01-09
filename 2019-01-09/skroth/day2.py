from collections import defaultdict

# part 1 stuff
def has_n_same(strid, n):
    freq = defaultdict(int)
    for c in strid:
        freq[c] += 1
    return n in freq.values()

def part1(strids):
    num_two = len([strid for strid in strids if has_n_same(strid, 2)])
    num_three = len([strid for strid in strids if has_n_same(strid, 3)])
    return num_two * num_three

# part 2 stuff
def how_close(str1, str2):
    num_diff = 0
    same = []
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            num_diff += 1
        else:
            same.append(str1[i])
    return num_diff, same

def part2(strids):
    goodies = None
    for strid in strids:
        for strid2 in strids:
            num_off, same_chrs = how_close(strid, strid2)
            if num_off == 1:
                return ''.join(same_chrs)
    
if __name__ == '__main__':
    with open('input.txt', 'rb') as f:
        ids = [l for l in f.read().split('\n') if l]
    print part1(ids)
    print part2(ids)
