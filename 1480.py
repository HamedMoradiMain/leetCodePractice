class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [];result.append(nums[0])
        for i in range(1,len(nums)):result.append(result[-1]+nums[i])
        return result
sol = Solution()
print(sol.runningSum(nums = [3,1,2,10,1]))