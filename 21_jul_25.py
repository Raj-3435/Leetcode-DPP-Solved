# Problem 1957. Delete Characters to Make Fancy String

class Solution:
    def makeFancyString(self, s: str) -> str:
        l=[]
        for i in s:
            if len(l)>=2 and l[-1]==l[-2]==i:
                continue
            l.append(i)
        return "".join(l)