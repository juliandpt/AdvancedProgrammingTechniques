def palindNum(num: int) -> bool:
    int_as_str = str(num)
    for i in range(len(int_as_str)//2):
        if int_as_str[i] != int_as_str[len(int_as_str) - i-1]:
            return False
    return True