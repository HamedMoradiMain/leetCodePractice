"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
"""
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result={}
        res = 0
        for num in nums:
            if num in result:
                res+=result[num]
                result[num] += 1
            else:
                result[num]=1
        print(result)
        return res
sol = Solution()
print(sol.numIdenticalPairs(nums = [1,2,3,1,1,3]))
