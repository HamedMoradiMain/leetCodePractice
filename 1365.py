class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in nums:
            count = 0
            for l in nums:
                if i > l: count += 1
            result.append(count)
        return result
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))