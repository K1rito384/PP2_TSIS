from itertools import permutations

def print_permutations(user_string):
    perm = permutations(user_string)
    for p in perm:
        print(''.join(p))

user_input = input("Enter a string: ")
print("Permutations:")
print_permutations(user_input)
