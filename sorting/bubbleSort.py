def bubbleSort(lis1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    print(list1)

if __name__ == "__main__":
    list1 = []
    n = int(input("Enter the length of the sorting array: "))
    for _ in range(n):
        list1.append(int(input("Enter a number for the array: ")))

    bubbleSort(list1)