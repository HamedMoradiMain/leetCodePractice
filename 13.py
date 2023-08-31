class Solution:
    def romanToInt(self, s: str) -> int:
        r = 0
        l = ['I','V', 'X', 'L', 'C', 'D', 'M']
        m = [1,5,10,50,100,500,1000]
        n = ['IV','IX','XL','XC','CD','CM']
        p = [4,9,40,90,400,900]
        for i in n:
            if i in s: 
                r+=p[n.index(i)]
                s=s.replace(i,"")
        print(s)
        for i in s: 
            if i in l: r+=m[l.index(i)]
        return r
sol = Solution().romanToInt("MCMXCIV")
print(sol)
