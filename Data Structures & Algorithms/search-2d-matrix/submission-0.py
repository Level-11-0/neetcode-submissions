class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Step 1: find candidate row via binary search
        top, bot = 0, ROWS - 1
        row = -1
        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row = mid          # target falls within this row's range
                break

        if row == -1:
            return False

        # Step 2: binary search within matrix[row]
        return self.binarySearch(matrix[row], target)

    def binarySearch(self, arr: List[int], target: int) -> bool:
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False