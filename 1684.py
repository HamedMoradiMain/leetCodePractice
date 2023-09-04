import re
class Solution(object):
    def countConsistentStrings(self, allowed, words) -> int:
        res = []
        for x in words:
            x=x.replace(allowed,'')
            if len(x) > 0: res.append(x)
        return len(words) - len(res)
sol = Solution()
print(sol.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))