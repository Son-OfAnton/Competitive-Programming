# 904. Fruit Into Baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_length = 0
        basket = {}
        
        for right in range(len(fruits)):
            basket[fruits[right]] = right
            
            if len(basket) > 2:
                min_index = min(basket.values())
                del basket[fruits[min_index]]
                left = min_index + 1
            max_length = max(max_length, right - left + 1)
            
        return max_length

# Basically the question asks us to return the maximum length of 
# a subarray which contains at most 2 types of fruits. So what we
# are going to do is placing fruits as a key in a basket dictionary 
# along with their last occuring index as a value. When our basket 
# contains more than 2 types of fruits we remove the a fruit which 
# has a last occuring index at a far left and placing the left pointer
# immediately after the fruit we just deleted. Then update the max 
# length by taking the max of its previous value and the current range
# between right and left pointers.
