n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a)
print(' '.join(map(str, a_sorted)))
