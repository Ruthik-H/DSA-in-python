fruits = [1, 2, 1]
dict1 = {}
left = 0
max_count=0
for i in range(len(fruits)):
    fruit = fruits[i]
    if fruit in dict1:
        dict1[fruit] += 1
    else:
        dict1[fruit] = 1
    while len(dict1)>2:
        dict1[fruit[left]]-=1
        if dict1[fruit[left]]==0:
            del dict1[fruit[left]]
        left+=1
    max_count=max(max_count,i-left+1)
print(max_count)
