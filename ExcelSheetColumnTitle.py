class Solution:
    # Method to convert a given number to an Excel column
    def convertToTitle(self, columnNumber: int) -> str:
       # initialize output string as empty
       result = ''
       while columnNumber > 0:
           # find the index of the next letter and concatenate the letter 
           # to the solution 
           # here index 0 corresponds to 'A', and
           # 25 corresponds to 'Z'
           index = (columnNumber -1) % 26
           result += chr(index + ord('A'))
           columnNumber = (columnNumber - 1) // 26
       return result[::-1]
if __name__ == "__main__":
    sol = Solution()
    sol.convertToTitle(28)