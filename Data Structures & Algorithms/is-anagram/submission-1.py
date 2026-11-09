class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in s_dict:
                s_dict[char] -= 1
            else:
                return False
        
        for val in s_dict.values():
            if val != 0:
                return False

        return True