from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        distance = defaultdict(lambda: -1)
        visited = set()
        dist_heap = [(0, k)]
        heapq.heapify(dist_heap)
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append([v, t])
        
        print(graph)

        while dist_heap:
            print(dist_heap)
            dist, current = heapq.heappop(dist_heap)
            if current in visited:
                continue
            visited.add(current)
            distance[current] = dist


            for v, t in graph[current]:
                if v not in visited:
                    heapq.heappush(dist_heap, (dist+t, v))

        
        # print(distance.items, distance.values())
        min_dist = min(distance.values())
        max_dist = max(distance.values())

        return -1 if min_dist == -1 or len(distance) < n else max_dist



