def sort_kamnem (list, last):
    if -1>=last:
        list.reverse()
        return
    i=list.index(max(list[0:last+1]))
    list.append(list[i])
    list.pop(i)
    sort_kamnem (list, last-1)

def sort_puzir (list, first):
    if first==len(list)
        return

    i=len(list)-1

    while i>0:
        if list[i]<list[i-1]:
            list[i] , list [i-1] = list [i-1], list[i]
        i-=1

    sort_puzir (list, first+1)

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
