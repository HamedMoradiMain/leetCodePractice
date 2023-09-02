class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:k=celsius+237.15;f=k-237.15*1.80+32.00;return[k,f]