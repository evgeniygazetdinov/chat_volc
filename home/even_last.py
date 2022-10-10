RIGHT = 'right'
LEFT = 'left'

def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    def check_each_word(word: str):
        new_word = word
        if RIGHT in word:
            new_word = word.replace(RIGHT, LEFT)
        return new_word
    res = [check_each_word(word) for word in phrases]
    return ",".join(res)

print("Example:")
print(left_join(("left", "right", "left", "stop")))

assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")