import matplotlib.pyplot as plot
import random

plot.ion()

def swapItems(list, index1, index2):
    """
    :return: Swaps two elements of a list
    """
    list[index1], list[index2] = list[index2], list[index1]
    return list


def makeList(length):
    output = [i for i in range(1, length + 1)]
    random.shuffle(output)
    return output


def bubbleSort(alist, graph):
    length = len(alist) - 1
    compare = range(0,length+1)
    counter = 0
    for i in range(0, length):
        swapped = False
        for j in range(0, length - i):
            if alist[j] > alist[j+1]:
                alist = swapItems(alist, j, j+1)
                counter += 1
                swapped = True
                if graph:
                    plot.clf()
                    plot.bar(compare,alist)
                    plot.pause(.001)
        if not swapped:
            break
    return counter


def cocktailShakerSort(alist):
    length = len(alist) - 1
    compare = range(0,length+1)
    up = True
    for i in range(0, length):
        swapped = False
        if up:
            for j in range(i/2, length - i/2):
                if alist[j] > alist[j+1]:
                    alist = swapItems(alist, j, j+1)
                    swapped = True
                    up = False
                    plot.clf()
                    plot.bar(compare,alist)
                    plot.pause(.001)
            if not swapped:
                break
        else:
            for j in range(length - (i-1)/2, (i-1)/2, -1):
                if alist[j] < alist[j-1]:
                    alist = swapItems(alist, j, j-1)
                    swapped = True
                    up = True
                    plot.clf()
                    plot.bar(compare,alist)
                    plot.pause(.001)
            if not swapped:
                break
    return alist


def selectSortReplace(alist, graph):
    length = len(alist)
    compare = range(0, length)
    count = 0
    for i in range(0, length):
        mindex = i
        for j in range(i, length):
            if alist[j] < alist[mindex]:
                mindex = j
        if mindex != i:
            count += 1
            list = swapItems(alist, i, mindex)
        if graph:
            plot.clf()
            plot.bar(compare,alist)
            plot.pause(.1)
    return count


def selectSortShift(alist, graph):
    length = len(alist)
    compare = range(0, length)
    output = []
    count = 0
    for i in range(0, length):
        mindex = 0
        listlen = len(alist)
        for j in range(0, listlen):
            if alist[j] < alist[mindex]:
                mindex = j
        if mindex != i:
            count += 1
            output.append(alist[mindex])
            alist.remove(alist[mindex])
        if graph:
            plot.clf()
            plot.bar(compare, output+alist)
            plot.pause(.1)
    return count


def insertSort(alist, graph):
    length = len(alist)
    compare = range(0, length)
    count = 0
    for i in range(length - 1):
        for j in range(i, -1, -1):
            count += 1
            if alist[j+1] < alist [j]:
                alist = swapItems(alist, j, j+1)
            else:
                break
            if graph:
                plot.clf()
                plot.bar(compare,alist)
                plot.pause(.1)
    return count


# Not Functional
def shellSort(alist, graph):
    length = len(alist)
    for i in range(length):
        interval = length//(2 ^ (i+1))
        for j in range(interval):
            return True


def quickSort(alist, start = 0, stop = -10):
    if stop == -10:
        stop = len(alist) - 1
    if stop - start < 1:
        return
    else:
        left = start
        right = stop
        pivot = alist[start]
        while left <= right:
            while alist[left] < pivot:
                left += 1
            while alist[right] > pivot:
                right -= 1
            if left <= right:
                swapItems(alist, left, right)
                left += 1
                right -= 1
        quickSort(alist, start, right)
        quickSort(alist, left, stop)


def mergeSort(blist):
    """
    :return: Merge sorts a list.
    """
    # Sorry for the list comp Becca :)
    if len(blist) <= 1:
        return
    else:
        fhalf = blist[:len(blist)/2]
        shalf = blist[len(blist)/2:]
        mergeSort(fhalf)
        mergeSort(shalf)
    nswr = [((fhalf.pop(0) if fhalf[0] < shalf[0] else shalf.pop(0)) if (len(fhalf) > 0 and len(shalf) > 0) else (fhalf.pop(0) if len(fhalf) > 0 else shalf.pop(0))) for i in range(len(blist))]
    for i in range(len(nswr)):
        blist[i] = nswr[i]





test = makeList(20)
mergeSort(test)
print test

def testSort(function):
    count = []
    for i in range(1000):
        test = makeList(100)
        count.append(function(test, False))
    return sum(count)/len(count)

"""
print testSort(bubbleSort)
print testSort(selectSortReplace)
print testSort(selectSortShift)
print testSort(insertSort)
"""
