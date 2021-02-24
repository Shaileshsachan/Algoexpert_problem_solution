def pivotPlace(list1, first, last):
    pivot = list1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:  # for descending change < | >
            left += 1
        while left <= right and list1[right] >= pivot:  # for descending change > | <
            right -= 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right

def quickSort(list1, first, last):
    if first < last:
        p = pivotPlace(list1, first, last)
        quickSort(list1, first, p-1)
        quickSort(list1, p+1, last)

list1 = [56, 26, 93, 17, 31, 44]
n = len(list1)
quickSort(list1, 0, n-1)
print(list1)