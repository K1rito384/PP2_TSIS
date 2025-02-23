import re
pattern6 = r"[ ,.]"
test_string6 = "Hello, world. How are you?"
print(re.sub(pattern6, ":", test_string6))
