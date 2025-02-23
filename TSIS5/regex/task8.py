import re
pattern8 = r"(?=[A-Z])"
test_string8 = "SplitAtUppercaseLetters"
print(re.split(pattern8, test_string8))