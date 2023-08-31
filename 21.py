class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        f = []
        if len(list1) and len(list2) == 0: return f
        else:
            for i in range(max(len(list1),len(list2))):
                print(i)
                if i != len(list1):
                    f.append(list1[i])
                if i != len(list2):
                    f.append(list2[i])
        return f
sol= Solution()
print(sol.mergeTwoLists(list1 = [], list2 = []))