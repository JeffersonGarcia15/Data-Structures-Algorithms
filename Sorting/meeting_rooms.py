# Time O(n^2) Auxiliary Space O(1)
# def meeting_rooms(intervals):
#     for i in range(len(intervals)):
#         for j in range(i + 1, len(intervals)):
#             a = intervals[i][0]
#             b = intervals[i][1]
#             c = intervals[j][0]
#             d = intervals[j][1]
#             if d < a or b < c:
#                 continue
#             else:
#                 return False
#     return True
# print(meeting_rooms([[0, 30], [5, 10], [15, 20]])) # False
# print(meeting_rooms([[7, 10], [2, 4]])) # True
# print(meeting_rooms([[0, 5], [10, 15]])) # True

# O(nlogn) Time and O(1) Auxiliary Space
def meeting_rooms(intervals):
    intervals.sort()
    for i in range(len(intervals)):
        if i == len(intervals) - 1:
            next_interval_start_time = float("inf")
        else:
            next_interval_start_time = intervals[i + 1][0]
            current_interval_end_time = intervals[i][1]
            if current_interval_end_time > next_interval_start_time:
                return False 
    return True
print(meeting_rooms([[0, 30], [5, 10], [15, 20]])) # False
print(meeting_rooms([[7, 10], [2, 4]])) # True
print(meeting_rooms([[0, 5], [10, 15]])) # True