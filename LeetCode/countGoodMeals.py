# https://leetcode.com/problems/count-good-meals/

class Solution:
    def getPairs(self, value, count) -> int:
        ans = 0

        for i in range(22):
            power_of_two = 2**i
            key = power_of_two - value

            if key in count:
                if key == value:
                    ans += (count[key] - 1)
                else:
                    ans += count[key]
        
        return ans
        
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        count = Counter(deliciousness)

        for value in deliciousness:
            ans += self.getPairs(value, count)
            
        ans //= 2
        ans %= (10**9) + 7
        
        return ans
    
