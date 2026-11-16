class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        curr = 0
        for bit in bin_n:
            curr += 1 if bit =='1' else 0
        
        return curr