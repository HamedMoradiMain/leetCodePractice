import string
class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        x = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l = string.ascii_lowercase;res = []
        for word in words:
            m = [x[l.index(i)] for i in word];f = "".join(m)
            if f not in res:res.append(f)
        return (len(res))
sol = Solution()
print(sol.uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))
        

        