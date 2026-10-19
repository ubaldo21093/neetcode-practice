from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_s = Counter(s)
        string_t = Counter(t)
        if string_s == string_t:
            return True
        else: 
            return False


        

