class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = {i: char for i, char in enumerate(s)}
        h2 = {i: char for i, char in enumerate(t)}

        flag = False

        if sorted(h1.values()) == sorted(h2.values()):
            flag = True

        return flag

