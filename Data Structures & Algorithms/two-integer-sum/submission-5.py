class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #Stores seen numbers in case compleement came previously

        for index, num in enumerate(nums):

            if (target - num) in seen:
                return [seen[target-num], index]

            seen[num] = index
