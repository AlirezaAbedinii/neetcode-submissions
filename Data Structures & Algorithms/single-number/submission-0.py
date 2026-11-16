from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        n = len(nums)
        return(nums.most_common(n)[-1][0])