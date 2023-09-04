import re
class Solution:
    def countAsterisks(self, s: str) -> int:
        patt = re.compile('\|(.*?)\|');matches=patt.finditer(s);res=''
        for item in matches:res+=item.group()
        return s.count('*') - res.count('*')
sol = Solution()
print(sol.countAsterisks(s = "l|*e*et|c**o|*de|"))