def max_digit(number: int) -> int:
    number = str(number)
    etalon = int(number[0])
    for digit in number:
        if int(digit) > etalon:
            etalon = digit
    return etalon


if __name__ == '__main__':
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
