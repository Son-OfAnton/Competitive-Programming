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
