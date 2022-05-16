def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    counter = 0
    run_append = False
    result = ''
    while text[counter] != end:
        if text[counter] == begin:
            run_append = True
        elif run_append:
            result+= text[counter]
        counter+=1
    return result


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    #
    # # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')