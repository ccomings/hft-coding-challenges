#!/usr/bin/env python
#
# Matt Schettler
# Nov 2018
# 
# https://github.com/ccomings/hft-coding-challenges/blob/master/2018-11-15/longest-substr-wo-repeating-chars.md
# 
import itertools


def len_longest_substr_no_repeat_chars(s):
    """ return the length of the longest substring of s that does not repeat any characters """
    return max((len(s[i:j]) for i, j in itertools.permutations(range(len(s)+1), 2) if i < j and (j - i) == len(set(s[i:j]))))


def main():

    # basic tests
    assert len_longest_substr_no_repeat_chars('a') == 1  # entire string
    assert len_longest_substr_no_repeat_chars('ab') == 2  # entire string
    assert len_longest_substr_no_repeat_chars('abc') == 3  # entire string
    assert len_longest_substr_no_repeat_chars('abcabcbb') == 3  # abc
    assert len_longest_substr_no_repeat_chars('bbbbb') == 1  # b
    assert len_longest_substr_no_repeat_chars('pwwkew') == 3  # kew
    
    # advanced tests
    assert len_longest_substr_no_repeat_chars('hello world, this is earth') == 11  # world, this
    assert len_longest_substr_no_repeat_chars(''.join(map(str, range(50)))) == 10  # 2345678910
    assert len_longest_substr_no_repeat_chars('qwertyuioplkjhgfdsazxcvbnm') == 26  # entire string
    assert len_longest_substr_no_repeat_chars('qwertyuioplkjhgfdsazxcvbnm0123456789') == 36  # entire string
    assert len_longest_substr_no_repeat_chars('qwerty@uioplk@jhgfds@azxcvb@nm0123@456789') == 13  # qwerty@uioplk

    print "well, it worked!"


if __name__ == '__main__':
    main()
