def insertionSort(list1):
    for i in range(1, len(list1)):
        current_element = list1[i]
        pos = i
        while current_element < list1[pos - 1] and pos > 0:
            list1[pos] = list1[pos - 1]
            pos = pos - 1
        list1[pos] = current_element

n = int(input("Enter the number of elements in list :"))
list1 = [int(input('Enter the number :')) for _ in range(n)]
insertionSort(list1)
print(list1)