class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        nex = 1
        if n == 1 or n == 0:
            return 1
        for i in range(n):
            ans = prev + nex
            prev, nex = nex, ans
        return ans