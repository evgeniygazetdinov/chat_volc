
def changing_direction(directions :list ) -> int:
    counter = 0
    # previos = directions[0]
    
    for one_direction in directions:
        if one_direction >= previos:
            previos = one_direction
        else:
            counter+= 1
            previos = 0
    return counter 


print(changing_direction(list(range(5))))

assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2