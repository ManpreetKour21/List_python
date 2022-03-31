a=[[1,3,1],[2,3,1],[4,2,1]]
i=0
b=[]
while i<len(a):
    sum=0
    j=0
    while j<len(a):
        sum=sum+a[i][j-1]
        j=j+1
    i=i+1   
print(sum)