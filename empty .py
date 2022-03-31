a=[1,2,[],4,5,[],6]
i=0
j=[]
while i<len(a):
    if a[i]!=[]:
        j.append(a[i])
    i=i+1
print(j)