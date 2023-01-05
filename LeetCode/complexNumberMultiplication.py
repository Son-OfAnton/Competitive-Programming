# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')
        
        num1_real = int(num1[0])
        num1_comp = int(num1[1][:-1])
        
        num2_real = int(num2[0])
        num2_comp = int(num2[1][:-1])        
        
        real = num1_real * num2_real - num1_comp * num2_comp
        comp = num1_real * num2_comp + num1_comp * num2_real
        
        return f"{real}+{comp}i"
        
