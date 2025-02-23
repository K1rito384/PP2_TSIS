import re
pattern9 = r"([A-Z])"
test_string9 = "InsertSpacesBetweenWords"
print(re.sub(pattern9, r" \1", test_string9).strip())