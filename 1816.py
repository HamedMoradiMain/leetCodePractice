class Solution(object):
    def truncateSentence(self, s: str, k: int) -> str:
        s = [x for x in s.split(" ")]
        return s[k]
sol = Solution()
sol.truncateSentence(s = "Hello how are you Contestant", k = 4)