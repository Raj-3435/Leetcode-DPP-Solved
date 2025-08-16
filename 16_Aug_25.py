# Problem 1323. Maximum 69 Number

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        l=[]
        count = 0 
        for i in num:
            if count == 0 and i != '9':
                l.append('9')
                count += 1
            else:
                l.append(i)

        return int("".join(l))