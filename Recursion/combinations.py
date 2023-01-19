def combinations(n, k):
    if k == 0 or k == n:
        return 1
    return combinations(n - 1, k - 1) + combinations(n - 1, k)
