def is_all_upper(text: str) -> bool:
    res = list(set(i.isupper for i in text if not i.isspace))
    result = res[0] if len(res) is 1 else False
    print(result)
    return result

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    is_all_upper('ALL UPPER') == True
    is_all_upper('all lower') == False
    is_all_upper('mixed UPPER and lower') == False
    is_all_upper('') == True
    is_all_upper('     ') == True
    is_all_upper('444') == True
    is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
