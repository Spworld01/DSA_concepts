nums=[5,10,-3,-1,-10,6]

def rearrange_(arr):
    n=len(arr)

    list=[]
    for i in range(0,n):
        if arr[i]>0:
            k=0
            list.append(list[k]==arr[i])
            k+=2
        else:
            arr[i]<0
            j=1
            list.append(list[j]==arr[i])
            j+=2

    return list

print(rearrange_(nums))

