def med_arr(arr):
    arr.sort()
    return arr[len(arr)//2]
arr=[1,3,5,2,4,6]
median=med_arr(arr)
print(median)