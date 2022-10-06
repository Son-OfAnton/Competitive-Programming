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

# A better solution
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        res = []
             
        for i, alpha in enumerate(s):
            last_seen[alpha] = i
            left, right = 0, -1

        for i, alpha in enumerate(s):
            if last_seen[alpha] > right:
                right = last_seen[alpha]
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        
        return res
    
# First we make a dictionary of alphabets. Then we place the right pointer 
# at the last seen index of an alphabet while we iterate over the string as 
# long as the last seen index of an alphabet is greater than the right pointer.
# When the index of an alphabet is equal to the right index, we can be sure that
# the substring between the two pointer is valid then we append its length to res.


