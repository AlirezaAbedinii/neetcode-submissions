class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        current = n

        while current != 1:
            new = 0
            str_curr = str(current)
            for digit in str_curr:
                digit = int(digit)
                new += digit**2
            if new in seen:
                return False
            current = new
            seen.add(current)
        
        return True


