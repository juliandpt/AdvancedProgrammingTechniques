array = [0, 1, 2, 3, 4, 5]

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

def searchItem(arr, elem):
    for i in range(len(arr)):
        if elem == arr[i]:
            return i
    return -1

def searchRec(arr, elem):
    return searchRec2(arr, elem, 0, len(arr)-1)

def searchRec3(arr, elem):
    return searchRec1(arr, elem, 0, len(arr)-1)

def searchRec1(arr, elem, l, r):
    if l == r:
        if arr[l] == elem:
            return l
        else:
            return -1
    e_m = arr[(l+r-1)//2]
    if e_m == elem:
        return (l+r-1)//2
    elif e_m > elem:
        #elem, si esta, esta a la izq de m
        return searchRec1(arr, elem, l, ((l+r-1)//2)-1)
    else:
        return searchRec1(arr, elem, ((l+r-1)//2)+1, r)

def searchRec2(arr, elem, l, r):
    if l == r:
        return arr[l] == elem
    e_m = arr[(l+r-1)//2]
    if e_m == elem:
        return True
    elif e_m > elem:
        #elem, si esta, esta a la izq de m
        return searchRec2(arr, elem, l, ((l+r-1)//2)-1)
    else:
        return searchRec2(arr, elem, ((l+r-1)//2)+1, r)

#printList(array)
print(searchItem(array, 4))
print(searchRec(array, 6))
print(searchRec3(array, 4))