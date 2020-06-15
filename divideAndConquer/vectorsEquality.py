def vectEquals(vector0: list, vector1: list, p: int, f: int):
    if p == f:
        return vector0[p] == vector1[p]
        
    return vectEquals(vector0, vector1, p, (p+f)//2) and vectEquals(vector0, vector1, ((p+f)//2)+1, f)