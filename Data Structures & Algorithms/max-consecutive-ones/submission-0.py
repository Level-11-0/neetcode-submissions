class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_number_of_consecutive_ones = 0
        sequential_ones = 0
        for i in (nums):
            sequential_ones += 1
            if(i == 0):
                sequential_ones = 0
            if sequential_ones > max_number_of_consecutive_ones:
                max_number_of_consecutive_ones = sequential_ones

        return max_number_of_consecutive_ones
