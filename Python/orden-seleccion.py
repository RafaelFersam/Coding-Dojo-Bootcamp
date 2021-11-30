def ordenamiento_seleccion(array):
    for i in range(0,len(array)):
        min_value = array[i]
        min_index = i
        for k in range(min_index + 1, len(array)):
            if array[k] < min_value:
                min_value = array[k]
                min_index = k
        temp = array[i]
        array[i] = min_value
        array[min_index] = temp
    return array
array = [2,5,6,4,8,9,3,1,0]

ordenamiento_seleccion(array)
print(ordenamiento_seleccion(array))

