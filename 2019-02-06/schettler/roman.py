# -*- coding: utf-8 -*-

int_roman_map = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # collect return value
        ret = []

        # loop through possible roman numerals
        for k, v in int_roman_map:

            # how many times does this letter fit in num
            d = num // k

            # append this manny letters to result
            ret.append(v * d)

            # subtract the value we just represented from num
            num -= k * d

        # make string
        return ''.join(ret)


s = Solution()
print s.intToRoman(14)
