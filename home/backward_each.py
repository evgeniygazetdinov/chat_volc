def backward_string_by_word(some_string: str) -> str:
    if some_string == "":
        return ""
    if len(some_string.split()) <= 2:
        spaces = ''
        how_many_spaces = some_string.count(' ')
        res = some_string.split()
        reverted_word = [word[::-1]for word in res]
        spaces += ' ' * how_many_spaces
        return spaces.join(reverted_word)
    elif len(some_string) > 2:
        # TODO make it more clean
        spaces = ''
        how_many_spaces = some_string.count(' ')
        res = some_string.split()
        reverted_word = [word[::-1]for word in res]
        return ' '.join(reverted_word)
    else:
        return some_string[::-1]

assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"
# TODO just count spaces beetween and write it
print(backward_string_by_word('ha ha ha   this is cool'))