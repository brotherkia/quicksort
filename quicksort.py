import random
def swap(lst,i,j):
    tmp = lst[i]
    lst[i]=lst[j]
    lst[j]=tmp


def pivotfunc(lst,s,e):
    p_index = random.randrange(0,len(lst))
    pointer = 0
    print(lst[p_index])
    for i in range(s,e):
        if lst[i]<= lst[pointer]:
            swap(lst,i,pointer)
            pointer +=1
    return p_index,pointer


def quickSort(lst,s,e):
    p_index,pointer = pivotfunc(lst, s, e)
    swap(lst,p_index,pointer)
# [7, 2, 6, 4, 1, 8, 3, 5] 5
arr = [7,2,6,5,1,8,3,4]
quickSort(arr, 0, 7)
print(arr)
