# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        top_elements = [i for i in freq.keys()]
        
        return [top_elements[i] for i in range(k)]
        
# First we make a dictionary of elements and their frequency.
# Then we will sort the dictionary by value that means by frequency.
# Then we will store the keys(the actual numbers in nums) in a list.
# Finally all we have to do is selecting the first k elements in the list.
