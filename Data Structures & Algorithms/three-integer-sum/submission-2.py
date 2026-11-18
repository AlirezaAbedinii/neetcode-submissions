class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        start = 0
        end = n = len(nums)
        outs = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            s = i + 1
            e = n-1
            while s < e:
                if s > i+1 and nums[s] == nums[s-1]:
                    s+=1
                    continue
                current = nums[s] + nums[e]            
                if current == -val:
                    outs.append([val, nums[s], nums[e]])
                    s += 1
                elif current < -val:
                    s += 1
                else:
                    e -= 1
            
            
        
        return outs







