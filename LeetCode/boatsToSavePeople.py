# 881. Boats to Save People

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        number_of_boats = 0
        i = 0
        j = len(people) - 1
        people.sort()

        while i <= j:
            remain = limit - people[j]
            j -= 1
            if people[i] <= remain:
                i += 1
            number_of_boats += 1

        return number_of_boats

# After sorting it will be easier to spot the heaviest 
# and the lighest person. Then we will check the possibility 
# of the lighest person with heaviest on one boat. If it 
# is valid we will place the lighest person else we will 
# only place the heaviest one.
