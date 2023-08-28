class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        x = [sum(x) for x in accounts]
        return (max(x))
sol = Solution()
print(sol.maximumWealth(accounts = [[1,2,3],[3,2,1]]))