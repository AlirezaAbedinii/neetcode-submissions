class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        first = 0
        sub = {s[0]: 0}
        max_sub = 1

        for i in range(1, len(s)):
            if s[i] not in sub or sub[s[i]] < first:
                sub[s[i]] = i
                
                
            else:
                
                max_sub = max(max_sub, i - first)
                first = sub[s[i]]+1
                sub[s[i]] = i
                
        
        max_sub = max(max_sub, len(s) - first)
        return max_sub
                
