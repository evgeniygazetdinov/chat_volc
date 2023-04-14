def find_order(text_order):
    res = {}
    for position, word in enumerate(text_order.split()):
        res[position] = word
    return res

def check_increase(list_with_numbers):
    res = False
    if len(list_with_numbers) <= 1:
        return res
    num_before = 0
    counter = 0 
    for num in list_with_numbers:
        if num > num_before:
            counter+=1
    if counter == len(list_with_numbers):
        res = True
    return res

def words_order(text: str, words: list) -> bool:
    cur_order = []
    order = find_order(text)
    for position, value in order.items():
        for word in words:
            # fix position check here
            if value == word:
                cur_order.append(position)
    is_increased = check_increase(cur_order)

    return is_increased
    


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
