# Write a recursive function that takes an array and returns all of its subsets. How many sets will it return?
# if [a, b, c] there are 3 ele then 2^3 = 8 subsets meaning {empty, [1], [2], [3], [1,2], [2,3], [1,3], [1,2,3]}

# O(2^n) time | O(2^n) space
def subsets(lst):
    output = [[]]
    for i in lst:
        
        output += [lst + [i] for lst in output] # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        # output.append([lst + [i] for lst in output]) [[], [[1]], [[2], [[1], 2]], [[3], [[1], 3], [[2], [[1], 2], 3]]]

    return output

print(subsets([1,2,3]))
