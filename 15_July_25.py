# Problem 3136
# https://leetcode.com/problems/valid-word/editorial

class Solution:
    def ispunct(self,word):
        for ch in word:
            if ch in string.punctuation:
                return True
        return False
    def isValid(self, word: str) -> bool:
        vowel = "aeiou"
        cons = "bcdfghjklmnpqrstvwxyz"
        word = word.lower()
        if (len(word)<3):
            return False
        elif(self.ispunct(word)):
            return False
        else:
            vcount = 0
            ccount = 0
            for i in word:
                if (i in vowel):
                    vcount = vcount+1
                elif(i in cons):
                    ccount = ccount+1
            if (vcount >=1 and ccount >= 1):
                return True
            else: 
                return False
                    