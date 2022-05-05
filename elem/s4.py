from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    res = []

    return [:`

if __name__ == '__main__':
    print("Example:")
    list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    list(remove_all_before([], 0)) == []
    list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
