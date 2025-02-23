import re
pattern5 = r"a.*b$"
test_string5 = ["ab", "axb", "a123b", "a_b", "aBCb", "abc"]
print([s for s in test_string5 if re.fullmatch(pattern5, s)])