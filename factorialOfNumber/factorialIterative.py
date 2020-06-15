def factIter(num: int) -> int:
    res = 1
    for i in range(1, num+1):
        res = res * i
    return res