# 2110. Number of Smooth Descent Periods of a Stock

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1] * len(prices)
        
        for i in range(len(prices) - 1):
            if prices[i + 1] == prices[i] - 1:
                dp[i + 1] = dp[i] + 1
        
        return sum(dp)
    
# A smooth period is a period consisting only one period 
# or if it consists multiple periods, the periods should
# in decreasing fashion with a difference of 1 between them.
# So, the question can be rephrased as the sum of the number 
#of smooth periods ending at each index.
