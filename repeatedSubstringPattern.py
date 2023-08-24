class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s = [x for x in s[0:len(s)]]
        ch = []
        for item in s:
            if item not in ch:
                ch.append(item)
                print(item)
        for i in ch:
            print(s.count(i))

if __name__ == "__main__":
    sol = Solution()
    sol.repeatedSubstringPattern(s = "abccbabac")