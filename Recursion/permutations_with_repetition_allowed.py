def permutations_with_repetition_allwed(n):
    def helper(n, slate):
        if n == 0:
            print(slate)
        else:
            for i in range(10):
                helper(n - 1, slate + str(i))
    helper(n, "")
print(permutations_with_repetition_allwed(10))