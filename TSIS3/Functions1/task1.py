def grams_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces

# Example usage
gram_value = 500  # Example: 500 grams
oz_value = grams_to_ounces(gram_value)
print(f"{gram_value} grams is equal to {oz_value:.2f} ounces.")
