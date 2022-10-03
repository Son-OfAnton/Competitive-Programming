# 274. H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        H_index = 0
        
        for i, val in enumerate(citations):
            if val > i:
                H_index += 1
            else:
                break
        
        return H_index

# The idea is to find the number of elements which 
# have a value greater than their index. 
