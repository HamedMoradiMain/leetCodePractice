class Solution(object):
    def isValid(self, s):
       l = ["(",
       ")",
       "{",
       "}",
       "[","]"]
       count = 0
       for item in l:
           if (s.count(item) % 2) == 0:
               count += 1
       if (count % 2 ) == 0:
           for item in l:
              if len(count)==2 and (s.count(item)) == 1:
                      return False
              else:
                return True
       else:
           return False
           
sol = Solution()
print(sol.isValid(s = "([)"))