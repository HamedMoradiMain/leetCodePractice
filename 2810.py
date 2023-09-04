class Solution(object):
    def finalString(self, s):
        r = [];s=[x for x in s]
        for i in range(0,len(s)):
            if s[i] == 'i':
                if len(r) == 0: 
                    r.append(s[i][::-1])
                    print(s)
                    #for l in range(0,i):s.remove(s[l])
                    print(s)
                else:
                    r.append("".join(s[i][::-1])+"".join(r[-1][::-1])) 
        print(r)


sol = Solution()
sol.finalString(s = "viwif")
        