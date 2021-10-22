def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 2, memo) + fibonacci(n - 1, memo)
    return memo[n]
