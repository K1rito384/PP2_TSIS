def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = unique_elements(original_list)
print("Original list:", original_list)
print("List with unique elements:", unique_list)