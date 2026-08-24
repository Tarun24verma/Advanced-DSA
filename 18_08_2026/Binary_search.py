def root(n):
    if n < 0:
        return None
    start = 0
    end = max(1, n)
    while end - start > 1e-9:
        mid = (start + end) / 2
        if mid**2 > n:
            end = mid
        else:
            start = mid
    print(mid)
root(25)