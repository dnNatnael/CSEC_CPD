colors = list(map(int, input().split()))
unique_colors = len(set(colors))
additional = max(0, 4 - unique_colors)
print(additional)
