word = input().strip()
uppercase_count = sum(1 for char in word if char.isupper())
lowercase_count = sum(1 for char in word if char.islower())
if uppercase_count > lowercase_count:
    corrected_word = word.upper()
else:
    corrected_word = word.lower()
print(corrected_word)
