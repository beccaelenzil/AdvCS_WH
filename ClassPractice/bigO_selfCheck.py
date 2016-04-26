def nSquaredMin(list):
    # This one is basically bubble sort
    for i in range(1, len(list)+1):
        for j in range(len(list)-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list[0]

def nMin(list):
    minimum = list[0]
    for i in range(len(list)):
        if list[i] < minimum:
            minimum = list[i]
    return minimum


alist = [1,245,43,137,4,537,2345,0,3465,3]
print nSquaredMin(alist)
print nMin(alist)