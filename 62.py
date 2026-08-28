#Unique paths 
m=3 #rows
n=3 #columns
grid=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if i==0 or j==0:  #just puting the staring matrix values as zeroes becuase anyways there is only one way
            grid[i][j]=1
        else:
            grid[i][j]=grid[i-1][j]+grid[i][j-1]  #this line is just adding the above and left 
print(grid[m-1][n-1])
