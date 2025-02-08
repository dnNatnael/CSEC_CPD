def total_calories(a1, a2, a3, a4, s):
    strip_calories = {'1': a1, '2': a2, '3': a3, '4': a4}
    total = 0
    for char in s:
        total += strip_calories[char]
    return total
a1, a2, a3, a4 = map(int, input().split())
s = input().strip()
print(total_calories(a1, a2, a3, a4, s))
