# https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.type_slot = defaultdict(int)
        
        self.type_slot[1] = big
        self.type_slot[2] = medium
        self.type_slot[3] = small        

    def addCar(self, carType: int) -> bool:
        if self.type_slot[carType] > 0:
            self.type_slot[carType] -= 1
            
            return True
        else:
            return False            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
