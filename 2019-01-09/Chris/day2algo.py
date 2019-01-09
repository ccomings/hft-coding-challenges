lines = [line.rstrip("\n") for line in open("day2input.txt")]

def checksum(array):
    two = 0
    three = 0
    for id in array:
        counter_dict = {}
        istwo = False
        isthree = False

        for ch in id:
            counter_dict[ch] = counter_dict.get(ch, 0) + 1

        for num in counter_dict.values():
            if num == 2:
                istwo = True
            elif num == 3:
                isthree = True
            else:
                continue

        if istwo:
            two += 1
        if isthree:
            three += 1

    print two * three

checksum(lines)

def findletters(array):

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            count = 0
            string = ""
            for k, ch in enumerate(array[i]):
                if count > 1:
                    break
                if ch != array[j][k]:
                    count += 1
                else:
                    string += ch
                    
            if count == 1:
                print array[i], array[j], string


findletters(lines)
