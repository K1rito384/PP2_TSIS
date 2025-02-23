import re
pattern2 = r"ab{2,3}"
test_string2 = ["abb", "abbb", "abbbb", "ab", "a"]
print([s for s in test_string2 if re.fullmatch(pattern2, s)])