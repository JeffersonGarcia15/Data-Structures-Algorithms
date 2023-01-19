# O(2n*n) Time and O(n) Space
def binary_strings(n):
    def helper(n, slate):
        if n == 0:
            print(slate)
        else:
            helper(n - 1, slate + "0")
            helper(n - 1, slate + "1")
            
    helper(n, "")
print(binary_strings(3))