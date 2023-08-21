class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        s = [x for x in s[0:len(s)]]
        s2 = [x for x in s[0:len(s)]]
        for i in range(0,len(s)):
           s2[indices[i]] = s[i]
        s2 =''.join(s2)
        return s2
if __name__ == "__main__":
    sol = Solution()
    sol.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])