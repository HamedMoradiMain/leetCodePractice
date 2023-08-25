class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        res = False
        if len(s1.strip()+s2.strip()+s3.strip()) == 0:
            res = True 
        return res
sol = Solution()
print(sol.isInterleave("","",""))