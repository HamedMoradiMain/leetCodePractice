class Solution:
    def equalFrequency(self, word: str) -> bool:
        #print(f'{}')
        word = [x for x in word[0:len(word)]]
        ch = []
        for item in word:
            if item not in ch:
                ch.append(item)
        for item in ch:
            print(item,"   ",word.count(item))
if __name__ == "__main__":
    sol = Solution()
    sol.equalFrequency('abcc')