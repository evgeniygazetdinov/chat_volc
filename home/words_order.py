def is_upper_list(some_list):
    begin = some_list[0]
    is_upper = []
    for one in some_list[1::]:
        if begin < one:
            is_upper.append(True)
        else:
            is_upper.append(False)
    is_only_one_way = len(set(is_upper)) == 1
    return is_only_one_way and list(set(is_upper))[0] == True


def words_order(text: str, words: list) -> bool:
    order = {}
    orders_from_word = []
    for position, word in enumerate(text.split(' ')):
        order[int(position)] = word

    for position, word in order.items():
        if word in words:
            # fix here i just across one example
            orders_from_word.append(position)
    return is_upper_list(orders_from_word)
    

    
print("Example:")
print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")