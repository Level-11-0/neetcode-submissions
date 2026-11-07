class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_number_of_consecutive_ones = 0
        sequential_ones = 0
        for i in nums:
            sequential_ones = sequential_ones + i if i else 0
            max_number_of_consecutive_ones = max(sequential_ones,max_number_of_consecutive_ones)

        return max_number_of_consecutive_ones
