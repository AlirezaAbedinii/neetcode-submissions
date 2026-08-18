class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        # current_combo= []
        def dfs(i, current_combo):
            
            remained = target - sum(current_combo)
            
            if remained == 0:
                res.append(current_combo.copy())
                return
            
            if i>= len(nums):
                return
            
            # Exclude
            
            for j in range(int(remained/nums[i])):
                current_combo.append(nums[i])
                dfs(i+1, current_combo)
            
            for j in range(int(remained/nums[i])):
                current_combo.pop()
            dfs(i+1, current_combo)

        dfs(0, [])
        return res

        