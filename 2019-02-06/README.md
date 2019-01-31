PROBLEM 1 https://leetcode.com/problems/merge-sorted-array/:
  Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

  Note:

  The number of elements initialized in nums1 and nums2 are m and n respectively.
  You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
  Example:

  Input:
  nums1 = [1,2,3,0,0,0], m = 3
  nums2 = [2,5,6],       n = 3

  Output: [1,2,2,3,5,6]



PROBLEM 2 https://leetcode.com/problems/integer-to-roman/:
  Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

  Symbol       Value
  I             1
  V             5
  X             10
  L             50
  C             100
  D             500
  M             1000
  For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

  Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

  I can be placed before V (5) and X (10) to make 4 and 9.
  X can be placed before L (50) and C (100) to make 40 and 90.
  C can be placed before D (500) and M (1000) to make 400 and 900.
  Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

  Example 1:

  Input: 3
  Output: "III"
  Example 2:

  Input: 4
  Output: "IV"
  Example 3:

  Input: 9
  Output: "IX"
  Example 4:

  Input: 58
  Output: "LVIII"
  Explanation: L = 50, V = 5, III = 3.
  Example 5:

  Input: 1994
  Output: "MCMXCIV"
  Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
