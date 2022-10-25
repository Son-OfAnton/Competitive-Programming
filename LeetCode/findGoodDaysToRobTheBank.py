# 2100. Find Good Days to Rob the Bank

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        count = 0
        left_sum = [0] * len(security)
        right_sum = [0] * len(security)
        res=[]

        for i in range(1, len(security)):
            if security[i - 1] >= security[i]:
                count += 1 
            else:
                count = 0
            left_sum[i] = count
            
        count = 0
        for i in range(len(security) -2, -1, -1):
            if security[i] <= security[i + 1]:
                count += 1
            else:
                count = 0
            right_sum[i] = count
        
        for i in range(len(security)):
            if left_sum[i] >= time and right_sum[i] >= time:
                res.append(i)
        
        return res

# First we make a list containing the number of consecutively increasing
# numbers to the left and right of the current number. Then we will iterate
# over it and check if the number of consecutively increasing to both sides
# is greater than or equal to time. If it is, we will store the index in a 
# result list.
    
