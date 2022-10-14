# 1894. Find the Student that Will Replace the Chalk

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        
        for index in range(len(chalk)):
            if k < chalk[index]:
                return index
            k -= chalk[index]
        
# If the sum of all chalks is greater than k we will circle back
# to the beginning so we just need k modulo sum of chalks and 
# assign it to k. Then we will subtract each chalk from k and 
# check if we ran out of chalks. If we ran out of chalks we return
# the student whose turn comes next.
    
