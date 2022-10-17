# 2140. Solving Questions With Brainpower

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cummulative_points = [0] * len(questions)

        for i in range(len(questions)-1, -1, -1):
            points = questions[i][0]
            brain_power = questions[i][1]
            
            cummulative_points[i] = points
            
            if i + brain_power + 1 < len(questions):
                cummulative_points[i] += cummulative_points[i + brain_power + 1]         

            if i + 1 < len(questions):
                cummulative_points[i] = max(cummulative_points[i], cummulative_points[i+1]) 

        return max(cummulative_points)
    

# We are iterating backwards. First we just do the question at index i.
# Then we check if we can do the next question after jumping brain_power 
# questions, if we can we add the its points. Then we take the max of the
# current calculated points of question[i] and the question[i+1]. After
# exiting the loop we will take the max of all cummulative points and take
# the highest points we came across.
