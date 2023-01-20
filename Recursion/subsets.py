# Time O(2^n * n) Space O(n)
def subsets(array):
    def helper(array, slate):
        if len(array) == 0:
            print(slate)
        else:
            # Exclude
            helper(array[1:], slate)
            # Include
            helper(array[1:], slate + array[0])
                
            
    helper(array, "")
print(subsets(["1", "2", "3"]))