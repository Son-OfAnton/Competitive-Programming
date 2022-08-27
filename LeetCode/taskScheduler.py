# 621.Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        arr = []
        
        for i in count.values():
            arr.append(i)
            
        arr.sort(reverse=True) 

        idle = (arr[0] - 1) * n 

        for i in range(1, len(arr)): 
            if arr[i] == arr[0]:
                idle += 1
            idle -= arr[i]

        if idle < 0:
            idle = 0
        
        total = 0
        
        for i in arr:
            total += i

        return total + idle
