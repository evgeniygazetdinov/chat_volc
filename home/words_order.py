def is_upper_list(some_list):
    if some_list:
        begin = some_list[0]
        is_upper = []
        for one in some_list[1::]:
            if begin < one:
                is_upper.append(True)
            else:
                is_upper.append(False)
        is_only_one_way = len(set(is_upper)) == 1 
        one_element_in_list = len(some_list) == 1 
        return is_only_one_way and list(set(is_upper))[0] == True or one_element_in_list
    else:
        return False


def words_order(text: str, words: list) -> bool:
    order = {}
    orders_from_word = []
    for position, word in enumerate(text.split(' ')):
        order[word] = int(position)
    if len(words) > len(set(words)):
        return False
    else:
        current_order_in_compared_list = {}
        for word in words:
            if word not in text:
                return False
            for value, ord in order.items():
                if word == value:
                    current_order_in_compared_list[value] = ord
                    # TODO defeat word not in list
        return is_upper_list(list(current_order_in_compared_list.values()))
    

    
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