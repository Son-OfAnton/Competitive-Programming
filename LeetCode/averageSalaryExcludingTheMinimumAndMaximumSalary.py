# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/?

class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = max(salary)
        min_salary = min(salary)
        salary_sum = divisor = 0

        for i in salary:
            if i != max_salary and i != min_salary:
                salary_sum += i
                divisor += 1

        return salary_sum / divisor
      
      
