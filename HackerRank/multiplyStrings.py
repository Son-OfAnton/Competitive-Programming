# https://leetcode.com/problems/multiply-strings/

class Solution:
    def toStringParser(self, char_digit: chr) -> int:
        char_int = {}
        
        for digit in range(10):
            str_form = str(digit)
            char_int[str_form] = char_int.get(str_form, 0) + digit
        
        return char_int[char_digit]
        
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = 0
        power = 0
        
        for char in reversed(num1):
            int_num1 += self.toStringParser(char) * 10**power
            power += 1
            
        int_num2 = 0
        power = 0
        
        for char in reversed(num2):
            int_num2 += self.toStringParser(char) * 10**power
            power += 1
            
        product = int_num1 * int_num2
        
        return str(product)
