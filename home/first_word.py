from re import S


import re

def first_word(text: str) -> str:
    """
    function returns the first word in a given text.
    """
    def find_word(word):
        pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
        pattern = re.compile(pattern, re.IGNORECASE)
        matches = re.search(pattern, text)
        return bool(matches)

    return re.sub(r'(^|[^\w]){}([^\w]|$)', text).strip().split()





print("Example:")
print(first_word("Hello world"))

# assert first_word("Hello world") == "Hello"
# assert first_word(" a word ") == "a"
# assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
# assert first_word("... and so on ...") == "and"
# assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")