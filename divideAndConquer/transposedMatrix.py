#Este apartado es un pseudocodigo, no es ejecutable

def traspose(M):
    if dimensión(M) == 4:
        return trasposeOf4(M)
    else:
        T[0,0] a [dim(M)/2,dim(M)/2] = trasponer(M[0,0] a [dim(M)/2,dim(M)/2]
        T[0,dim(M)/2] a [(dim(M)/2)+1,dim(M)] = transponer(M[(dim(M)/2)+1,0] a [dim(M),dim(M)/2])
        T[dim(M)/2,0] a [dim(M),dim(M)/2] = transponer(M[0,(dim(M)/2)+1] a [(dim(M)/2)+1,dim(M)])
        T[(dim(M)/2)+1,(dim(M)/2)+1] a [dim(M),dim(M)] = transponer(M[(dim(M)/2)+1,(dim(M)/2)+1] a [dim(M),dim(M)]

def trasposeOf4(M):
    for i in range(x_o,x_f):
        for j in range(y_o,y_f):
            m_dest[i][j] = m_t[i][j]