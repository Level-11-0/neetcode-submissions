class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low_speed, high_speed = 1, max(piles)

        while low_speed <= high_speed:
            eating_speed = (low_speed + high_speed) // 2
            total_hours = 0

            for pile in piles:
                total_hours += -(-pile // eating_speed)

            if total_hours > h:
                low_speed = eating_speed + 1   # too slow, speed up
            else:
                high_speed = eating_speed - 1  # works, try slowing down

        return low_speed  # smallest speed that finishes within h