
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
