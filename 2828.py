class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        x = [x+extraCandies for x in candies]
        res = []
        for i in x:
            if i >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
sol = Solution()
print(sol.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))