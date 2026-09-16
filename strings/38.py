n=4
result="1"
for i in range(n-1):
    ans=""
    j=0

    while j<len(result):
        count=1
        while j+1<len(result) and result[j]==result[j+1]:
            count+=1
            j+=1

        ans+=str(count)+result[j]
        j+=1
    result=ans

print(result)
