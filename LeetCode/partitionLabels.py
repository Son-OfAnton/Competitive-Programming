# 763. Partition Labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = right = 0
        length = len(s)
        ans = []

        for right in range(length):
            if set(s[left:right + 1]).intersection(set(s[right + 1:])) == set():
                ans.append(right - left + 1)
                left = right + 1

        return ans
    
# First we place both pointers at index 0 and increment the right one until
# the substring between the two bounds and the rest of the list has no 
# letters in common. When the right pointer reaches an index which satisfy
# the above condition we will append the length of the substring between 
# the pointers to the res list and place the left pointer at the front of the 
# right one.
