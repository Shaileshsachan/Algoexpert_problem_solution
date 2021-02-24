def shellSort(list1):
    gap = len(list1) // 2
    while gap > 0:
        for i in range(gap, len(list1)):
            current_element = list1[i]
            pos = i
            while pos >= gap and current_element < list1[pos - gap]:
                list1[pos] = list1[pos - gap]
                pos = pos - gap
            list1[pos] = current_element
        gap = gap // 2

n = int(input("Enter the number of elements in list :"))
list1 = [int(input('Enter the number :')) for _ in range(n)]
shellSort(list1)
print(list1)