def bubbleSort(arr):
    lenght = len(arr) - 1
    #print(lenght)
    #bucles for para las pasadas
    for i in range(0, lenght):
        print(f"pasada #{i + 1}")
        #bucles for para las comparaciones
        for j in range(0, lenght):
            print(f'comparacion: {arr[j]} > {arr[j + 1]} ')
            if arr[j] > arr[j + 1]:
                print(f'intercambiar: {arr[j]} x {arr[j + 1]}')
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
                
    return arr
arr = [5,8,1,0,3,2]

print(f"antes de ordenar{arr}")
print(f"despues de ordenar{bubbleSort(arr)}")

