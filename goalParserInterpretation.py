import re 
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()","o").replace("(al)","al")
        return command
if __name__ == "__main__":
    sol = Solution()
    sol.interpret(command = "(al)G(al)()()G")