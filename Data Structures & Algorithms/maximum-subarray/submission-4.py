class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find_start(starting_index = 0):
            
            if nums[starting_index] > 0 or starting_index == n-1:
                return starting_index


            

            for i in range(starting_index + 1, n):
                if nums[i] > 0 or nums[i] > nums[i-1]:
                    return i
            return starting_index

        
        n = len(nums)

        if n == 1:
            return nums[0]

        start = find_start()
        current = start
        cur_sum = nums[start]
        best = cur_sum

        while  current < n-1:
            
            current += 1
            if nums[current] >= 0:
                cur_sum += nums[current]
            else :
                best = max(cur_sum, best)
                cur_sum += nums[current]
                if cur_sum < 0:
                    start = find_start(current)
                    current = start
                    cur_sum = nums[start]
                    
        
        
        return max(cur_sum, best)

                




                

