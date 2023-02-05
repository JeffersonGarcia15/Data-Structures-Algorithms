# O(n) Time and O(n) Space
def insert_interval(intervals, new_interval):
    bail_index = len(intervals) - 1
    results = []
    for i in range(len(intervals)):
        if intervals[i][1] < new_interval[0] or new_interval[1] < intervals[i][0]:
            # No overlap
            results.append(intervals[i])
        else:
            bail_index = i
            break
    results.append(new_interval)
    for i in range(bail_index, len(intervals)):
        if results[-1][1] < intervals[i][0] or intervals[i][1] < results[-1][0]:
            # No overlap
            results.append(intervals[i])
        else:
            results[-1][0] = min(results[-1][0], intervals[i][0])
            results[-1][1] = max(results[-1][1], intervals[i][1])
            
    return results
print(insert_interval([[1, 3], [6, 9]], [2, 5])) # [[1, 5], [6, 9]]
print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])) # [[1, 2], [3, 10], [12, 16]]
