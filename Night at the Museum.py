def min_rotations(s):
    current = 'a'
    total = 0
    for char in s:
        diff = abs(ord(char) - ord(current))
        total += min(diff, 26 - diff)
        current = char
    return total
s = input().strip()
print(min_rotations(s))
