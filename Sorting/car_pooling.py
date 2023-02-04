import heapq
# Time O(nlogn) Auxiliary Space O(n)
def car_pooling(trips, capacity):
    min_heap = []
    heapq.heapify(min_heap)
    passengers = 0
    for i in range(len(trips)):
        trips.sort(key=lambda x: x[1])
        if i == len(trips) - 1:
            next_start = float("inf")
        else:
            next_start = trips[i + 1][1]
        passengers += trips[i][0]
        heapq.heappush(min_heap, (trips[i][2], trips[i][0]))
        if passengers > capacity:
            return False
        while len(min_heap) != 0 and min_heap[0][0] <= next_start:
            old_passengers = min_heap[0][1]
            heapq.heappop(min_heap)
            passengers -= old_passengers
    return True
        
        
print(car_pooling([[2, 1, 5], [3, 3, 7]], 4)) # False
print(car_pooling([[2, 1, 5], [3, 3, 7]], 5)) # True
print(car_pooling([[2, 1, 5], [3, 5, 7]], 3)) # True
print(car_pooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11)) # True