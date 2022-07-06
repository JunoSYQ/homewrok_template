def  MergeSort(list, temp, start, end):
    if start < end:
        middle = int((start + end) / 2)
        MergeSort(list, temp, start, middle)
        MergeSort(list, temp, middle + 1, end)
        MergeLists(list, temp, start, middle, end)
def MergeLists(list, temp, start, middle, end):
    global MergeCount
    global MergeSize
    #if middle-start and len(MergeSize)<=5:
    MergeSize.append(middle-start+1)
    MergeSize.append(end-middle)
    i = start
    while i <= middle:
        temp[i] = list[i]
        i = i + 1
    i = start
    j = middle+1
    k = start
    while i <= middle and j <= end:
        MergeCount = MergeCount + 1
        if temp[i] <= list[j]:
            list[k] = temp[i]
            k = k+1
            i = i+1
        else:
            list[k] = list[j]
            k = k + 1
            j = j + 1
    while i <= middle:
        list[k] = temp[i]
        k = k + 1
        i = i + 1
