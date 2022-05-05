def end_zeros(num: int) -> int:
    num = str(num)
    count = 0
    for i in num:
        if i == '0':
            count+= 1
        else:
            count = 0
    print(count)
    return count



end_zeros(0)
end_zeros(1)
end_zeros(101)
end_zeros(100100)
