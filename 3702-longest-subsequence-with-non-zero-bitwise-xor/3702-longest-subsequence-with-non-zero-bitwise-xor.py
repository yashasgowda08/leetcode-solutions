class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        n = len(nums)
        x = 0
        non_zero = False

        for num in nums:
            x ^= num
            if num != 0:
                non_zero = True

        if x != 0:
            return n

        if not non_zero:
            return 0

        return n - 1