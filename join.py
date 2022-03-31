# a= [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# i=0
# string=""
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         string=string+(a[i][j])
#         j+=1
#     i+=1
# print(string)


n= [1,2,3,1,2,2]
i=0
b=[]
while i<len(n):
    if n[i] not in b:
        b.append(n[i])
    i=i+1
print(b)


# a=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)



