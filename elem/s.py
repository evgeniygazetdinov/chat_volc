def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence."""
    frequi = {}
    for a in data:
        if a not in frequi.keys():
            frequi[a] = 0
        
        if a in frequi.keys():
            frequi[a] += 1
    key = list(frequi.keys())
    val = list(frequi.values())
    s = key[val.index(max(val))]
    
    print(s)
    return s

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
