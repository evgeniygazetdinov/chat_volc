from datetime import datetime

def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    first_date = datetime(year=int(a[0]), month=int(a[1]), day=int(a[2]))
    second_date = datetime(year=int(b[0]), month=int(b[1]), day=int(b[2]))
    return abs((second_date - first_date).days)


print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

print("The mission is done! Click 'Check Solution' to earn rewards!")