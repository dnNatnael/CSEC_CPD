import math
Y, W = map(int, input().split())
max_roll = max(Y, W)
favorable = 6 - max_roll + 1
numerator = favorable
denominator = 6
gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd
print(f"{numerator}/{denominator}")
