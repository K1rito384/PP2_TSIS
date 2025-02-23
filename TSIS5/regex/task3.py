import re
pattern3 = r"[a-z]+_[a-z]+"
test_string3 = ["hello_world", "test_string", "helloWorld", "test_string_123"]
print([s for s in test_string3 if re.fullmatch(pattern3, s)])