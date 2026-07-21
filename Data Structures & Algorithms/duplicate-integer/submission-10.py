class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        no_dup = set()

        for i in range(len(nums)):
            current = nums[i]
            
            if current in no_dup:
                return True
            
            no_dup.add(current)
        
        return False