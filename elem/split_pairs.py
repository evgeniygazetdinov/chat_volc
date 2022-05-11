def split_pairs(a):
    # first shithole solution
    def append_before(some_list):
        my_string = ''
        result = []
        for i in range(len(some_list)):
            
            if i%2 ==0:
                my_string+= some_list[i]
            if i%2 !=0:
                my_string += some_list[i]
                result.append(my_string)
                my_string = ''
            
        return result

    if len(a)%2 !=0 and len(a)!=0:
        a+= '_'
    elif len(a) == 0:
        return []
    return append_before(a)



if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")