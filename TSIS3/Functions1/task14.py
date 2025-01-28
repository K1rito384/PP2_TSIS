from unique_elements_list import unique_elements, is_palindrome, histogram

original_list = [1, 3, 3, 5, 7, 7, 9]
unique_list = unique_elements(original_list)
print("Original list:", original_list)
print("Unique elements:", unique_list)

word = "level"
print(f"Is '{word}' a palindrome?", is_palindrome(word))

print("Histogram for [3, 5, 2]:")
histogram([3, 5, 2])