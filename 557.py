class Solution:
    def reverseWords(self, s: str) -> str:
        res = [x[::-1] for x in s.split()]
        return " ".join(res)
sol = Solution()
print(sol.reverseWords(s = "Let's take LeetCode contest"))