def SelectonSort(list1):
    print(f'Unsorted Array: {list1}')
    for i in range(len(list1) - 1):
        min_index = i
        for j in range(i+1, len(list1)):
            if list1[j] < list1[min_index]:
                min_index = j
        if list1[i] != list1[min_index]:
            list1[i], list1[min_index] = list1[min_index], list1[i]
    return (list1)

if __name__ == "__main__":
    n = int(input(f'Enter the length of number to sort: '))
    list1 = [int(input("Enter the number: ")) for _ in range(n)]
    print(SelectonSort(list1))




