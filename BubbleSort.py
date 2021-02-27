def BubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
        counter += 1
    return array

array = [12, 23, 34,121, 11, 787, 23]
print(BubbleSort(array))