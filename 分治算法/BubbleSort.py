def BubbleSort(list,n):
    global BubbleCount
    numberOfPairs = n
    swappedElements = True
    while swappedElements:
        numberOfPairs = numberOfPairs - 1
        swappedElements = False
        for i in range(numberOfPairs):
            BubbleCount = BubbleCount+1
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swappedElements = True
