def factRec(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * factRec(num-1)