import re 
class Solution(object):
    def sortSentence(self, s):
        x = s.split()
        l = [i for i in range(0,len(x))]
        for item in x:
            c = int (item[-1]) - 1 
            l[c]=item[:-1]
        return " ".join(l)
sol = Solution()
sol.sortSentence(s = "is2 sentence4 This1 a3")