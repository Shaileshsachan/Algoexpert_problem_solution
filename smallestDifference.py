# O(nlog(n) + m(log(m)) time  |  O(1) space
def smallestDifference(arrayone, arraytwo):
    arrayone.sort()
    arraytwo.sort()
    idxone = 0
    idxtwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxone < len(arrayone) and idxtwo < len(arraytwo):
        firstNum = arrayone[idxone]
        secondNum = arraytwo[idxtwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxone += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxtwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return  smallestPair
