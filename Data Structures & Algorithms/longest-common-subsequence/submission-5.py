class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * m for _ in range(n)]
        

        dp[0][0] = 1 if text1[0] == text2[0] else 0
        if n == 1:
            return (text1[0] in text2)*1
        if m == 1:
            return (text2[0] in text1)*1
        # dp[0][1] = 1 if text1[0] in text2[0:2] else 0
        # dp[1][0] = 1 if text2[0] in text1[0:2] else 0

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = (text1[0] in text2[0:j+1])*1
                elif j == 0:
                    dp[i][j] = (text2[0] in text1[0:i+1])*1
                
                elif text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[n-1][m-1]




