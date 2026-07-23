class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        no_white_s = lower_s.replace(" ", "")
        
        alnum_s = "".join(char for char in no_white_s if char.isalnum())
        # return alnum_s

        i = 0
        j = len(alnum_s)-1
        while(i<j):
            if alnum_s[i] != alnum_s[j]:
                return False
            
            i += 1
            j -= 1
        return True
