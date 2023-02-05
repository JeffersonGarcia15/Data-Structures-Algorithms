import heapq
# O(nlogn) Time and O(n) Space
# def merge_intervals(intervals):
#     result = []
#     answer = [float("inf"), float("-inf")]
#     min_heap = []
#     intervals.sort()
#     heapq.heapify(min_heap)
#     for i in range(len(intervals)):
#         if i == len(intervals) - 1:
#             next_start = float("inf")
#         else:
#             next_start = intervals[i + 1][0]
#         heapq.heappush(min_heap, (intervals[i][1] * -1, intervals[i][0] * -1))
#         while len(min_heap) != 0 and (min_heap[0][0] * -1) < next_start:
#             large, small = min_heap[0]
#             answer[0] = min(small * -1, answer[0])
#             answer[1] = max(large * -1, answer[1])
#             heapq.heappop(min_heap)
#             if len(min_heap) == 0:
#                 result.append(answer) 
#         answer = [float("inf"), float("-inf")]
#     return result

def merge_intervals(intervals):
    intervals.sort()
    results = [intervals[0]]
    for i in range(len(intervals)):
        if results[-1][1] < intervals[i][0] or intervals[i][1] < results[-1][0]:
            results.append(intervals[i])
        else:
            results[-1][0] = min(results[-1][0], intervals[i][0])
            results[-1][1] = max(results[-1][1], intervals[i][1])
    return results
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])) # [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]])) # [[1, 5]]
print(merge_intervals([[1,4],[0,2],[3,5]])) # [[0, 5]]
