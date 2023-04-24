

def sort_by_ext(files):
    extension = [one.split('.')[-1] for one in files]
    sorted_extension = sorted(extension)
    res = []
    for file in files:
        for ext in sorted_extension:
            if ext in file:
                files.insert(sorted_extension.index(ext), file)
    return res

# TODO FIX THIS ADD FUNCTION FOR SORTIONG
print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

# These "asserts" are used for self-checking
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
#     "1.aa",
#     "1.bat",
#     "2.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
#     ".bat",
#     "1.aa",
#     "1.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
#     ".aa",
#     ".bat",
#     "1.bat",
#     "1.cad",
# ]
# assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
#     "1.aa",
#     "1.bat",
#     "1.cad",
#     "1.aa.doc",
# ]
# assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
#     "1.aa",
#     "1.bat",
#     "1.cad",
#     ".aa.doc",
# ]

# print("The mission is done! Click 'Check Solution' to earn rewards!")