class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        
        for i in range(len(nums)):
            current = nums[i]
            if target - current in set_nums:
                second_number = target - current
                for j in range(i+1, len(nums)):
                    if nums[j] == second_number:
                        return [i, j]
