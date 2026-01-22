def filter_and_sort_evens(numbers):
    return sorted([x for x in numbers if x % 2 == 0])

def count_character_frequency(text):
    freq = {}
    for char in text.lower():
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example calls
print(filter_and_sort_evens([3, 1, 4, 1, 5, 9, 2, 6]))
print(count_character_frequency("Hello World"))
