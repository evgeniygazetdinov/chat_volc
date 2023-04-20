# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    words = 0
    digits = 0
    good_len = False
    for one in password:
        if one.isdigit():
            digits+=1
        elif not one.isdigit() or not one.isspace():
            words+=1
    has_some_digits = digits != 0 and digits != len(password)
    has_some_words = words != 0 and words !=len(password)
    good_len = len(password) > 6
    combinated = has_some_digits and has_some_words 

    result = good_len and  combinated
    return result   





print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")