arr=[1,5,3,7,2,8,6] 
def bubble_sort(arr): 
    n=len(arr)#7
    for i in range(n-1):#6 
        for j in range(0,n-i-1):#7-0-1=6, go till 8.
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(*bubble_sort(arr),sep=",")
#best case time complexity:O(N) already sorted
#worst case time complexity:O(N)
#compare only adjacent ites=ms in array.