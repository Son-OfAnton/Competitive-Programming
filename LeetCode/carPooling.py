# 1094. Car Pooling

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        station_pass = []
        
        for pass_num, start, end in trips:
            station_pass += [[start,pass_num]]
            station_pass += [[end,-pass_num]]
        
        curr_size = 0
        station_pass.sort()
                
        for station, pass_num in station_pass:
            curr_size += pass_num
            if curr_size > capacity:
                return False
            
        return True
    
# First we make a list which contains a list([stop, passenger number]).
# Then we add the number of passengers at the starting station which is 
# quite similar to how passengers enter the bus in a trip. And we subtract
# the number of passengers at the last station because the bus drops them off.
# Then we sort the list based on the station. Then we start accumulating the 
# number of passengers at each station if the number of passengers exceeds 
# the capacity we return False otherwise True.
