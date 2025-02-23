import re
pattern4 = r"[A-Z][a-z]+"
test_string4 = ["Hello", "World", "hello", "TEST", "Test"]
print([s for s in test_string4 if re.fullmatch(pattern4, s)])