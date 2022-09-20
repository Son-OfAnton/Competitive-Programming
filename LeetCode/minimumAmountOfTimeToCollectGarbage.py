# 2391. Minimum Amount of Time to Collect Garbage

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = list(accumulate(travel))
        dicti = {}
        time = 0
        for i in range(len(garbage)):
            if 'G' in garbage[i]:
                dicti['G'] = i
            if 'P' in garbage[i]:
                dicti['P'] = i
            if 'M' in garbage[i]:
                dicti['M'] = i
            time += len(garbage[i])
        for i in dicti:
            if dicti[i] > 0:
                time += travel[dicti[i] - 1]
        
        return time
