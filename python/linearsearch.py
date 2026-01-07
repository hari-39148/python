from re import search

arr=[1,2,3,4,5]
x=int(input("enter a number:"))
n=len(arr)
isfound=False
for i in range(n):
    if arr[i] == x:
        print("target is found")
        isfound=True
if isfound == False:
    print("element not found")
