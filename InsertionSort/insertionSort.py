def insertionSort(arr):
    arr = list(arr)
    for i in range(1, len(arr)): 
        it = arr[i] 
        j = i-1
        while j >= 0 and it < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = it
        print("El array en la iteracion {} es: {}".format(i, arr))