# a=[2,[2,3],4,[2,5]]
# i=0     
# sum=0
# c=[]
# while i<len(a):
#     j=0                       
#     while j<=a[i]:
#         sum=sum+int(i[j])
#         c.append(sum)
#         j=j+1
#     print(c)
#     i+=1
# a=[2,[2,3],4,[2,5]]
# i=1
# c=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     c.append(sum)
#     i+=2
# print(c)

# a=[["l"],["a"],["x"],["m"],["i"]]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

a=[1,2,3,4]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
    i+=1
print("even",b)
print("odd",c)



