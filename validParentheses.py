class Solution:
    def isValid(self, s: str): #-> bool:
        s1 =s.split("()")
        print(s1)
if __name__ == "__main__":
    sol = Solution()
    sol.isValid("()[]{}")