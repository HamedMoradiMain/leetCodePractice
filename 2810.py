import re
class Solution(object):
    def finalString(self, s):
        res =''
        for i in s:
            if i != 'i':res+=i
            else: res = res[::-1]
        return res


sol = Solution()
sol.finalString(s = "wivif")
        