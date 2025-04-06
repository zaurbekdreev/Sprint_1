def digit_root(num: int) -> int:
    if 0 <= num < 10:
        return num
    string = sum(map(lambda i: int(i), list(str(num))))
    return digit_root(int(string))
