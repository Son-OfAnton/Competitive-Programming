# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k
        summ = sum(cardPoints[right:])
        max_score = summ
        
        while right < len(cardPoints):
            summ += cardPoints[left] - cardPoints[right]
            max_score = max(max_score, summ)
            left += 1
            right += 1
            
        return max_score
    
# First we add the last k elements of cardPoints and set the right 
# pointer at the kth place from the last and left at index 0. Then 
# We will deduct the number at right and add number at the left if
# we get a larger summ than before we update max_score. Then we 
# increase both left and right and repeat until right reaches the end.
    

            
