import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res=[]
        for i in sorted(sentence):
            if i not in res:res.append(i)
        print(len(res))
        if "".join(res).lower() == string.ascii_lowercase:return True
        else:return False
        
sol = Solution()
print(sol.checkIfPangram('thequickbrownfoxjumpskoverthelazydog'))