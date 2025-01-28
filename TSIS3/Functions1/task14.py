import random

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

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    guesses = 0

    while True:
        print("Take a guess.")
        try:
            guess = int(input())
            guesses += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = unique_elements(original_list)
print("Original list:", original_list)
print("List with unique elements:", unique_list)

word = "madam"
print(f"Is '{word}' a palindrome?", is_palindrome(word))

print("Histogram:")
histogram([4, 9, 7])

guess_the_number()

from unique_elements_list import unique_elements, is_palindrome, histogram

original_list = [1, 3, 3, 5, 7, 7, 9]
unique_list = unique_elements(original_list)
print("Original list:", original_list)
print("Unique elements:", unique_list)

word = "level"
print(f"Is '{word}' a palindrome?", is_palindrome(word))

print("Histogram for [3, 5, 2]:")
histogram([3, 5, 2])