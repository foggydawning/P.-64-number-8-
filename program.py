def sort_kamnem (list, last):
    if -1>=last:
        list.reverse()
        return
    i=list.index(max(list[0:last+1]))
    list.append(list[i])
    list.pop(i)
    sort_kamnem (list, last-1)

def sort_puzir (list):
    if len(list)==1:
        return list

    i=len(list)-1

    while i>0:
        if list[i]<list[i-1]:
            list.insert(i-1, list.pop(i))
        i-=1

    li = sort (list[1:])
    del list[-1:0:-1]

    for k in range (0, len(li)):
        list.append(li[k])

    return list

def quicksort (list, min, max):
    if min>=max:
        return

    i=min
    j=max
    pivot = list[(j-i)//2+i]

    if i<=j:
        while list[i]<pivot and j!=i:
            i+=1
        while list[j]>pivot and j!=i:
            j-=1

        if i <= j:
            list[i], list[j]=list[j], list[i]
            i+=1
            j-=1
            sort ( list, min, j )
            sort ( list, i, max )
