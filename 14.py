class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans=""
        v=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(len(first),len(last)):
            print(i)
           #print(first[i])
            #print(last[i])
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
s = Solution()
print(s.longestCommonPrefix(strs=["flower","flow","flight"]))