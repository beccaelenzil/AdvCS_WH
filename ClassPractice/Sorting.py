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


def bubbleSort(list, graph):
    length = len(list) - 1
    compare = range(0,length+1)
    counter = 0
    for i in range(0, length):
        swapped = False
        for j in range(0, length - i):
            counter += 1
            if list[j] > list[j+1]:
                list = swapItems(list, j, j+1)
                swapped = True
                if graph:
                    plot.clf()
                    plot.bar(compare,list)
                    plot.pause(.001)
        if not swapped:
            break
    return counter


def cocktailShakerSort(list):
    length = len(list) - 1
    compare = range(0,length+1)
    up = True
    for i in range(0, length):
        swapped = False
        if up:
            for j in range(i/2, length - i/2):
                if list[j] > list[j+1]:
                    list = swapItems(list, j, j+1)
                    swapped = True
                    up = False
                    plot.clf()
                    plot.bar(compare,list)
                    plot.pause(.001)
            if not swapped:
                break
        else:
            for j in range(length - (i-1)/2, (i-1)/2, -1):
                if list[j] < list[j-1]:
                    list = swapItems(list, j, j-1)
                    swapped = True
                    up = True
                    plot.clf()
                    plot.bar(compare,list)
                    plot.pause(.001)
            if not swapped:
                break
    return list


def selectSortReplace(list, graph):
    length = len(list)
    compare = range(0, length)
    count = 0
    for i in range(0, length):
        mindex = i
        for j in range(i, length):
            count += 1
            if list[j] < list[mindex]:
                mindex = j
        if mindex != i:
            list = swapItems(list, i, mindex)
        if graph:
            plot.clf()
            plot.bar(compare,list)
            plot.pause(.1)
    return count


def selectSortShift(list, graph):
    length = len(list)
    compare = range(0, length)
    output = []
    count = 0
    for i in range(0, length):
        mindex = 0
        listlen = len(list)
        for j in range(0, listlen):
            count += 1
            if list[j] < list[mindex]:
                mindex = j
        if mindex != i:
            output.append(list[mindex])
            list.remove(list[mindex])
        if graph:
            plot.clf()
            plot.bar(compare,output+list)
            plot.pause(.1)
    return count


def insertSort(list):
    True


def testSort(function):
    count = []
    for i in range(1000):
        test = makeList(100)
        count.append(function(test, False))
    return sum(count)/len(count)

print testSort(bubbleSort)
print testSort(selectSortReplace)
print testSort(selectSortShift)