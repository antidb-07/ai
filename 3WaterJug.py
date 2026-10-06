print("Dharmik Bosamia")
print("53013240021")
def dfs(x,y,target):
    print(x,y,target)
    if x==target or y==target:
        exit()

    if x+y<=n and x>0:
        dfs(0,x+y,target)

    if x+y>n and y<n:
        dfs(x-(3-y),3,target)

    if x==m:
        dfs(0,y,target)

    if y==n:
        dfs(x,0,target)

    if x==0:
        dfs(m,y,target)

    if y==0:
        dfs(x,n,target)

m,n,target = 4,3,2
print(dfs(0,0,target))  