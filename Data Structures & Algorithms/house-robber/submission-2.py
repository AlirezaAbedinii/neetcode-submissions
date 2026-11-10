class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[2]+nums[0], nums[1])
        
        for i in range(3, n):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        return max(dp[n-1], dp[n-2])
