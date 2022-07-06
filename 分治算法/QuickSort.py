def QuickSort(list, first, last):
    if first < last:
        pivot = PivotList(list, first, last)
        QuickSize.append(pivot - first)
        QuickSize.append(last - pivot)
        QuickSort(list, first, pivot - 1)
        QuickSort(list, pivot + 1, last)

def PivotList(list, first, last):
    global QuickCount
    global QuickSize
    PivotValue = list[first]
    PivotPoint = first
    for index in range(first+1, last):
        QuickCount = QuickCount + 1
        if list[index] < PivotValue:
            PivotPoint = PivotPoint + 1
            list[PivotPoint], list[index] = list[index], list[PivotPoint]
    list[first], list[PivotPoint] = list[PivotPoint], list[first]
    return PivotPoint
