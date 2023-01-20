def permutations_without_repetition_allowed(array):
    def helper(array, slate):
        if len(array) == 0:
            print(slate)
        else:
            for i in range(len(array)):
                helper(array[:i] + array[i + 1:], slate + array[i])
    helper(array, "")
        
print(permutations_without_repetition_allowed(["a", "b", "c"]))