class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        far = celsius * (9/5) + float(32)
        kelv = celsius + 273.15
        ans = [kelv,far]
        return ans