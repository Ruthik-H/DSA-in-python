people = [3,2,2,1]
limit = 3
count=0
a=0
b=len(people)-1
people.sort()
while a<=b:
    if people[a]+people[b]<=limit:
        count+=1
        a+=1
        b-=1
    else:
        count+=1
        b-=1
print(count)
