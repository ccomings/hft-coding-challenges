
def longest_substr(in_str):
    """ Given a string, find the longest substring without repeating characters."""
    end = len(in_str)
    curr = ''
    longest = ''

    for c in in_str:
        if c not in curr:
            curr += c
        else:
            if len(curr) > len(longest):
                longest = curr
            curr = '' + c
    return longest

def solution(in_str):
    """ Given a string, find the length of the longest substring without repeating characters. Your function should take the input string and return an integer. """
    return len(longest_substr(in_str))


if __name__ == '__main__':
    TEST_STRS = {
        'abcabcbb': 3,
        'bbbbb': 1,
        'pwwkew': 3
    }
    for k, v in TEST_STRS.iteritems():
        print "longest in {} is {}".format(k, longest_substr(k))
        print "solution('{}') == {}".format(k, str(v))
        assert solution(k) == v
