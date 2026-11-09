class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        if len(s) <= 1:
            return True

        if (s[0] == s[-1]):
            return self.isPalindrome(s[1:-1])
        
        return False