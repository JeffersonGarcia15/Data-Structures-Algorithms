def towers_of_hanoi(n, src, dst, aux):
    if n == 1:
        print(f"move disk from {src} to {dst}")
    else:
        towers_of_hanoi(n - 1, src, aux, dst)
        print(f"move disk from {src} to {dst}")
        towers_of_hanoi(n - 1, aux, dst, src)
print(towers_of_hanoi(3, 'a', 'b', 'c'))