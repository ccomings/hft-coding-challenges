from collections import deque
# note, incomplete


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # stuff into a deque for efficient popping
        # nums1 comes in with odd padded values, we remove those
        stack1 = deque(nums1[:n])
        stack2 = deque(nums2)

        return [stack1.popleft() if stack1 and stack1[0] < stack2[0] else stack2.popleft() for _ in range(m)] + list(stack1) + list(stack2)


# https://leetcode.com/problems/merge-sorted-array/
s = Solution()

nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

print s.merge(nums1, m, nums2, n)

