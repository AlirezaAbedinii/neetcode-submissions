class Solution:
    def climbStairs(self, n: int) -> int:
        ways = {}
        ways[0] = 1
        ways[1] = 2
        
        for counter in range(2, n):
            ways[counter] = ways[counter-1] + ways[counter-2]

        return ways[n-1]
        
        