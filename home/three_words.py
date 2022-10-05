


def checkio(words: str) -> bool:
    # add your code here
    def true_counter(bool_list: list) -> bool:
        """
        count true in result array for undestand has it more 3 -> if more 3 return TRUE
        """
        counter = 0
        pointer = 0
        while(counter < 3):
            
            if pointer == len(bool_list):
                break
            result = bool_list[pointer]
            pointer += 1
            if result:
                counter += 1
            else:
                counter = 0
        return counter == 3


    def check_word(my_string: str) -> bool:
        """
        check only one word 
        false if it digit
        true if it word
        """
        res = False
        for word in my_string:
            if not word.isdigit():
                res = True
        return res

    def check_strings(word_strings: str) -> bool:
        """
        separate string by words for check each word
        """
        result_strings = []
        result = word_strings.split(' ')
        for res in result:
            result_strings.append(check_word(res))
        return true_counter(result_strings)

    return check_strings(words)


print("Example:")
print(checkio("Hello World hello"))

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False
assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True