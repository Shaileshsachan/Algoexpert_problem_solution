def BinarySearch(list1, key):
    low = 0
    high = len(list1) - 1
    found = False
    while low <= high and not found:
        mid = (high + low) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print("Key Found")
    else:
        print("Key is not Found")



list1 = [23, 1,4, 2, 3]
list1.sort()
print(list1)
key = int(input("Enter the key to find in the list: "))
BinarySearch(list1, key)
# list1 = []
# n = int(input("Enter the number of elements of a list:"))
# list1 = [list1.append(int(input("Enter the number :"))) for _ in range(n)]
# list1.sort()
# BinarySearch(list1, 7)
