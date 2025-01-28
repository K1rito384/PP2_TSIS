def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def histogram(int_list):
    for num in int_list:
        print('*' * num)

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = unique_elements(original_list)
print("Original list:", original_list)
print("List with unique elements:", unique_list)

word = "madam"
print(f"Is '{word}' a palindrome?", is_palindrome(word))

print("Histogram:")
histogram([4, 9, 7])