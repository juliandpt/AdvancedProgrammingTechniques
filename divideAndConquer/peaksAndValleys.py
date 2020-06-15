def peaksAndValleys(vector: list, p, f):
    if p == f:
        findPeaksAndValleys(vector, vector[f])
    else:
        m = (p+f)/2
        peaksAndValleys(vector, p, m)
        peaksAndValleys(vector, m+1, f)
    return vector[f]

def findPeaksAndValleys(vector: list, v):
    cont = 0
    if cont < len(vector)-1:
        cont += 1

        if v > vector[cont] and v > vector[cont-2]:
            print("pico hayado en la posicion {}".format(v))

        if v < vector[cont] and v < vector[cont-2]:
            print("valle hayado en la posicion {}".format(v))