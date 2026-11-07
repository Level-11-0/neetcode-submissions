class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        reversing_pointer = len(arr)-1
        greatest_value_pointer = -1
        for val in reversed(arr):
            arr[reversing_pointer] = greatest_value_pointer
            greatest_value_pointer = val if val > greatest_value_pointer else greatest_value_pointer
            reversing_pointer -= 1
        return arr