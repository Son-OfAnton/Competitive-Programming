# 1561. Maximum Number of Coins You Can Get

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        counter = 0
        max_coins = 0
        second_highest = len(piles) - 2
        
        while counter < second_highest:
            counter += 1
            max_coins += piles[second_highest]
            second_highest -= 2
        
        return max_coins
        
