#rotate an array by 90 degree
m = [[1,2,3]
    ,[4,5,6]
    ,[7,8,9]]

for i in range(len(m)):
    for j in range(i,len(m)):
        m[i][j],m[j][i]=m[j][i],m[i][j]   # to transpose the array  basically just to swap  
# using the reverse keyword 
# for row in m:
#     row.reverse()
# print(m)

# Reverse each row manually
for i in range(len(m)):
    left = 0
    right = len(m[i]) - 1

    while left < right:
        m[i][left], m[i][right] = m[i][right], m[i][left]
        left += 1
        right -= 1
print(m)

