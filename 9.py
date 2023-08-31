class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = [i for i in str(x)]
        r.reverse()
        if "".join(r) == str(x): return True
        else: return False
        
sol=Solution().isPalindrome(x=-121)
print(sol)