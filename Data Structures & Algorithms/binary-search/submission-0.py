class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] > target:
            return -1
        if nums[end] < target:
            return -1

        while (start < end-1):
            if nums[start] > target:
                return -1
            if nums[end] < target:
                return -1
            
            candid = int((start+end)/2)
            if nums[candid] == target:
                return candid
            elif nums[candid] > target:
                end = candid
            else:
                start = candid
        
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
