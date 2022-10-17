# 2140. Solving Questions With Brainpower

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        total_points = [0] * len(questions)

        for i in range(len(questions)-1, -1, -1):
            points = questions[i][0]
            brain_power = questions[i][1]
            
            total_points[i] = points
            
            if i + brain_power + 1 < len(questions):
                total_points[i] += total_points[i + brain_power + 1]         

            if i + 1 < len(questions):
                total_points[i] = max(total_points[i], total_points[i+1]) 

        return total_points[0]
    

# We are iterating backwards. First we just do the question at index i.
# Then we check if we can do the next question after jumping brain_power 
# questions, if we can we add the its points. Then we take the max of the
# current calculated points of question[i] and the question[i+1]. After
# exiting the loop we will take total_points[0] since it contains
# the largest point we came across.
