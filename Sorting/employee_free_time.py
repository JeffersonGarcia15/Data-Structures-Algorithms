# O(n^2) Time and O(n) Space
# def employee_free_time(schedule):
#     intervals = []
#     results = []
#     answer = []
#     for temp in schedule:
#         for elem in temp:
#             intervals.append(elem)
#     intervals.sort()
#     results.append(intervals[0])
#     for i in range(len(intervals)):
#         if results[-1][1] < intervals[i][0] or intervals[i][1] < results[-1][0]:
#             # No overlap
#             results.append(intervals[i])
#         else:
#             results[-1][0] = min(results[-1][0], intervals[i][0])
#             results[-1][1] = max(results[-1][1], intervals[i][1])
    
#     for i in range(len(results) - 1):

#         next_start = results[i + 1][0]
#         answer.append([results[i][1], next_start])
#     return answer

# O(nlogk) Time where n is the number of add/delete ops in MinHeap and k is the size of the heap || O(n) Space
import heapq
def employee_free_time(schedules):
    min_heap = []
    results = [[float("-inf"), float("-inf")]]
    heapq.heapify(min_heap)
    for i in range(len(schedules)):
        heapq.heappush(min_heap, (schedules[i][0][0], i, 0))
    
    while len(min_heap) > 0:
        start, ilist, pos = heapq.heappop(min_heap)
        if results[-1][1] < start or schedules[ilist][pos][1] < results[-1][0]:
            # No overlap
            results.append([start, schedules[ilist][pos][1]])
        else:
            results[-1] = [min(results[-1][0], start), max(results[-1][1], schedules[ilist][pos][1])]
        pos += 1
        if pos < len(schedules[ilist]):
            heapq.heappush(min_heap, (schedules[ilist][pos][0], ilist, pos))   
            
    list_of_free_time = []
    for i in range(1, len(results) - 1):
        list_of_free_time.append([results[i][1], results[i + 1][0]])
    
    return list_of_free_time
    
print(employee_free_time([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]))
print(employee_free_time([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]))
