# O(log(n)) time | O(log(n)) space
def BinarySearch(array, target):
    return BinarySearchHelper(array, target, 0, len(array) - 1)

def BinarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    match = array[middle]
    if target == match:
        return middle
    elif target < match:
        return BinarySearchHelper(array, target, left, middle -1)
    else:
        return BinarySearchHelper(array, target, middle + 1, right)

# O(log(n)) time | O(1) space
def Binary(array, target):
    return binarySearch(array, target, 0, len(array) - 1)

def binarySearch(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        match = array[middle]
        if target == match:
            return middle
        elif target < match:
            right = middle - 1
        else:
            left = middle + 1
    return -1

array = [1, 2, 33, 45, 56, 77]
print(Binary(array, 33))
