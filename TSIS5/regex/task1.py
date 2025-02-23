import re
pattern1 = r"ab*"
test_string1 = ["a", "ab", "abb", "ac", "abc"]
print([s for s in test_string1 if re.fullmatch(pattern1, s)])