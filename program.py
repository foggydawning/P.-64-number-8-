
def sort_kamnem (list):
    if len (list)==1:
        return list

    i=list.index(max(list))
    list.append(list[i])
    list.pop(i)

    li = sort (list[0:-1])
    del list[0:len(li)]

    for k in range (len(li)-1, -1, -1):
        list.insert(0,li[k])

    return(list)


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
