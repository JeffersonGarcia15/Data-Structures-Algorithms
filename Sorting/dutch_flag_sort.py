# Using QuickSort results in a time execution fail
# import random
# def dutch_flag_sort(balls):
#     hashMap = {"R": 0, "G": 1, "B": 2}
#     """
#     Args:
#     balls(list_char)
#     Returns:
#     list_char
#     """
#     # Write your code here.
#     def helper(balls, start, end):
#         #Base Case
#         if start >= end:
#             return
#         # Combine Step
#         smaller = start
#         pivot_idx = random.randint(start, end)
#         balls[start], balls[pivot_idx] = balls[pivot_idx], balls[start]
#         for bigger in range(start + 1, end + 1):
#             if hashMap[balls[start]] > hashMap[balls[bigger]]:
#                 smaller += 1
#                 balls[bigger], balls[smaller] = balls[smaller], balls[bigger]
#         balls[start], balls[smaller] = balls[smaller], balls[start]
        
#         # Divide Step
#         helper(balls, start, smaller - 1)
#         helper(balls, smaller + 1, end)
#     helper(balls, 0, len(balls) - 1)
#     print("ANSWER", balls)
#     return balls

def dutch_flag_sort(balls):
    red = -1
    white = -1
    for idx in range(len(balls)):
        if balls[idx] == "G":
            white += 1
            balls[white], balls[idx] = balls[idx], balls[white]
        elif balls[idx] == "R":
            white += 1
            balls[white], balls[idx] = balls[idx], balls[white] 
            red += 1
            balls[white], balls[red] = balls[red], balls[white] 
    return balls
print(dutch_flag_sort(["G", "B", "G", "G", "R", "B", "R", "G"]))