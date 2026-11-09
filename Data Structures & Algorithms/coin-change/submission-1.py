class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # min_coins_for[value]

        dp[0] = 0 # base case: 0 coins make 0

        for target in range(1, amount + 1): # for each amount, try every coin
            for coin in coins:
                remainder = target - coin
                if remainder >= 0 and dp[remainder] != float('inf'):
                    dp[target] = min(
                        dp[target],
                        1 + dp[remainder]
                    )

        return dp[amount] if dp[amount] != float('inf') else -1