class Solution:
    def maxDepth(self, s: str) -> int:
        s1 = [x for x in s];s2 = [x for x in s[::-1]];r=0;l=0;res=0
        for i in range(0,len(s1)):
            if s1[i] == "(":r+=1
            if s2[i] == ")":l+=1
            if "+" in s1[i]:res+=1
            if "+" in s2[i]:res+=1
            if r ==3 and l == 3:
                return res
                
sol = Solution()
print(sol.maxDepth(s = "(1)+((2))+()+(((3)))"))