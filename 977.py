n=int(input("Enter the number of elements:"))
arr=list(map(int,input("Enter the elements:").split()))
for i in range(len(arr)):
    arr[i]=arr[i]**2
arr.sort()
print(arr)
