"""Add examples with maps and normal use"""

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers: list[int] = []

# tipical way to get squared numbers
for num in numbers:
    squared_numbers.append(num ** 2)

print(numbers)
print(squared_numbers)

# using map function
def square(num: int) -> int:
    return num ** 2

squared_numbers_map = list(map(square, numbers))
print(squared_numbers_map)