"""This module contains examples with use cases of filter with pairs of values."""

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs: list = []

# tipical way to filter pairs
for num in numbers:
    if num % 2 == 0:
        pairs.append(num)

print(numbers)
print(pairs)

# using filter with lambda function
def is_pair(num: int) -> bool:
    return num % 2 == 0


pairs_filter = filter(is_pair, numbers)
print(list(pairs_filter))