def quickSort(arr, p, f): 
    if p < f: 
        part = particion(arr, p, f) 
        quickSort(arr, p, part-1) 
        quickSort(arr, part+1, f)

def particion(arr, p, f): 
    i = (p-1)         
    pivote = arr[f]     
  
    for j in range(p, f): 
        if   arr[j] <= pivote: 
            i = i+1 
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[f] = arr[f], arr[i+1] 
    return (i+1)