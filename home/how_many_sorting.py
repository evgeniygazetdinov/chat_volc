def changing_direction(elements: list) -> int:
    counter_changing = 0
    begin = elements[0]
    for elem in elements:
        if elem >= begin:
            begin = elem
        else:
            counter_changing += 1
    return counter_changing


print("Example:")
# print(changing_direction([1, 2, 3, 4, 5]))

# assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
# assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
