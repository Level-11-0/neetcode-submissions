class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightMax = -1
        for i in range(n - 1, -1, -1):
            arr[i], rightMax = rightMax, max(arr[i], rightMax)  # careful: see note
        return arr