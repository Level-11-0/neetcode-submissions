class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        while True:
            try:
                nums.remove(val)
                k -= 1
            except ValueError:
                break
        return k