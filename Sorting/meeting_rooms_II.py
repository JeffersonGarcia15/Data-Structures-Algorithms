# Time O(nlogn) Space O(n)
import heapq
def meeting_rooms_ii(intervals):
    intervals.sort()
    min_heap = []
    heapq.heapify(min_heap)
    global_max = 0
    for i in range(len(intervals)):
        if i == len(intervals) - 1:
            next_interval = float("inf")
        else:
            next_interval = intervals[i + 1][0]
        heapq.heappush(min_heap, intervals[i][1])
        global_max = max(global_max, len(min_heap))
        
        # End all intervals
        while len(min_heap) != 0 and min_heap[0] <= next_interval:
            heapq.heappop(min_heap)
    return global_max
print(meeting_rooms_ii([[0, 30], [5, 10], [15, 20]])) # 2
print(meeting_rooms_ii([[7, 10], [2, 4]])) # 1
print(meeting_rooms_ii([[0, 5], [10, 15]])) # 1
print(meeting_rooms_ii([[0, 30], [5, 16], [15, 20], [28, 29]])) # 3