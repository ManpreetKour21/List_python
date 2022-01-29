list=[7,41,21,13,0,5]
i=0
while i<len(list):
    j=0
    while j<i:
        if list[i]<list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        j+=1
    i+=1
print(list)