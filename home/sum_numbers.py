


def sum_numbers(text: str) -> int:
    def split_string(text: str) -> list:
        return text.split(' ')
    
    list_with_words = split_string(text)
    digits_for_sum = []
    for word in list_with_words:
        if word.isdigit():
            digits_for_sum.append(word)
    if not len(digits_for_sum):
        return 0
    return sum([int(digit) for digit in digits_for_sum])


print("Example:")
print(sum_numbers("hi"))

assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
