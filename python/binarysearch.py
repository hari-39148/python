def binarysearch(arr,target,n):
    min=0
    max=n-1
    
    while min<=max:
        mid=(min+max)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid] <= target):
            min=mid+1
        else:
            max=mid-1        
arr=[1,2,3,4,5,6]
target=int(input("enter the target"))
n=len(arr)
r=binarysearch(arr,target,n)
if r:
    print("element found")
else:
    print("element not found")