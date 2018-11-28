def find_the_substring_length(string):
    letter_dict = {}
    result = 0
    counter = 0
    for i, ch in enumerate(string):
        if ch in letter_dict:
            if counter > result:
                result = counter
            letter_dict = {}
            counter = 0
        letter_dict[ch] = True
        counter += 1
    return result

def main():
    print find_the_substring_length("abcabcbb")
    print find_the_substring_length("bbbbb")
    print find_the_substring_length("pwwkew")

if __name__ == '__main__':
    main()
