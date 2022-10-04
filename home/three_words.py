def checkio(words: str) -> bool:
    # add your code here
    def check_word(my_string: str) -> bool:
        res = False
        for word in my_string:
            if not word.isdigit():
                res = True
        return res

    def check_strings(word_strings: str) -> bool:
        result_strings = []
        result = word_strings.split(' ')
        for res in result:
            result_strings.append(check_word(res))
        if False in result_strings:
            return False
        result = [x for x in result_strings if x]
        return len(result) >= 3 

    return check_strings(words)


print("Example:")
print(checkio("Hello World hello"))

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False
assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True