#Union of two sorted arrays
# num1=[1,2,3,5]
# num2=[3,4,5,5,7,8]
# arr=[]
# for i in num1:
#     arr.append(i)
# for j in num2:
#     if j not in num1:
#         arr.append(j)
# for x in range(len(arr)-1):
#     if arr[x]>arr[x+1]:
#         arr[x],arr[x+1]=arr[x+1],arr[x]
# print(arr)


# same question with the 2 pointer approach 
num1=[1,2,3,5]
num2=[3,4,5,5,7,8]

arr=[]
i=0
j=0
for i in range(len(num1)):
    for j in range(len(num2)):
        if num1[i]<num2[j]:
            arr.append(num1[i])
            if num2[j]<num1[i]:
                arr.append(num2[j])
                if num1[i]==num2[j]:
                    arr.append(num1[i])
print(arr)