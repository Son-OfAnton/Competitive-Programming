# https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        fahrenheit = 1.8 * celsius + 32
        kelvin = celsius + 273.15

        return [kelvin, fahrenheit]
