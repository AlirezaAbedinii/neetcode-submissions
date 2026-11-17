from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # numset = set(nums)
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        freq = [(-frequency[num], num) for num in frequency]
        heapq.heapify(freq)
        topk = []
        for i in range(k):
            topk.append(heapq.heappop(freq)[1])

        return topk