from typing import Any, Iterable
import math


def split_list(items):
    def find_half(len_list):
        return math.ceil(len_list / 2)
    border_for_first = find_half(len(items))
    first = []
    second = []
    for item in range(len(items)):
        if item < border_for_first:
            first.append(items[item])
        else:
            second.append(items[item])
    return [first, second]






print("Example:")
print(list(split_list([1, 2, 3, 4, 5, 6])))
print(split_list(["banana", "apple", "orange", "cherry", "watermelon"]))
assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"], 
]
assert list(split_list([1])) == [[1], []]
assert list(split_list([])) == [[], []]

# print("The mission is done! Click 'Check Solution' to earn rewards!")