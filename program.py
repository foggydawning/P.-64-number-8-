def sort_kamnem (list, last, per=1):
    if -1>=last:
        list.reverse()
        print("Количество перестановок при методе 'камня' =", per)
        return
    i=list.index(max(list[0:last+1]))
    list.append(list[i])
    list.pop(i)
    per+=1
    sort_kamnem (list, last-1)

def sort_puzir (list, first=0,per=0):
    if first==len(list):
        print("Количество перестановок при использовании метода 'пузырька' =", per)
        return

    i=len(list)-1

    while i>0:
        if list[i]<list[i-1]:
            list[i] , list [i-1] = list [i-1], list[i]
            per+=1
        i-=1

    sort_puzir (list, first+1)

s=[0]
def quicksort (list, min, max,s):
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
            print("!")
            s[0]+=1
            i+=1
            j-=1
            quicksort ( list, min, j,s)
            quicksort ( list, i, max,s)
