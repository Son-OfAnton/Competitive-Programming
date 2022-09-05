# 1545. Find Kth Bit in Nth Binary String

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return "0"
            else:
                string = ""
                for i in helper(n-1):
                    if i == '0':
                        string += '1'
                    else:
                        string += '0'

                x = helper(n-1) + "1" + string[::-1]
                return x

        return helper(n)[k - 1]
