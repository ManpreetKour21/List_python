# a=[34,27,6,4,7,3]
# i=0
# # b=[]
# while i<len(a):
#     b=[]
#     j=0
#     while j<2:
#         b.append(a[j])
#         j=j+1
#         i=i+1
#     print(b)
#     i=i+1
# print(b)

# a=[34,27,6,4,7,3]
# i=0
# # b=[]
# while i<len(a):
#     b=[]
#     j=0
#     while j<2:
#         b.append(a[j])
#         j=j+1
#         i=i+1
#     print(b)

# a=[34,27,6,4,7,3]
# i=0
# while i<len(a):
#     b=[]
#     j=0  

#     while j<i:
#         b.append(a[j])
#         if j==1:
#             break
#         j=j+1
#     i=i+1
#     print(b)




# a=[6,7,8,9,5,7]
# i=0
# j=1
# # b=[]
# while i<len(a):
#     # b=[]
#     # b.append(a[i])
#     # b.append(a[j])
#     i=i+2
#     j=j+2
#     print(a)


# list1=[[0],[1,2,3],[6,7,8,10,11],[23,24]]
# i=0
# lis=[]
# while i<len(list1):
#     count=0
#     j=0
#     while j<len(list1[i]):
#         count=count+1
#         j=j+1
#     lis.append(count)
#     i=i+1
# print(lis)


# a=[34,27,6,4,7,3] 
# i=0
# j=1
# d=[]
# while i<len(a):
#     b=[]
#     sub=a[i]-a[j]
#     d.append(sub)
#     i=i+2
#     j=j+2
# print(d)



# # a=['a b c','x y z','a b ','1 2 2 1']
# # b=[]
# # i=0
# # c=0
# # while i<len(a):
# #     if a[i] :
# #         b.append(a[i])
# #         c=c+1
# #     i+=1
# # print(b,"=",c)


# # list=['aba','xyz','aba','1221']
# # i=0
# # count=0
# # while i<len(list):
# #     j=0
# #     while j<len(list[i]):
#         if list[i][0]==list[i][-1]:
#             count=count+1
#             print(count,list[i])
#             break
#         j=j+1
#     i=i+1



# l=['abc', 'xyz', 'aba', '1221']
# i=0
# c=0
# a=[]
# while i<len(l):
#     if len(l[i])>0 and l[i][0]==l[i][-1]:
#         a.append(l[i])
#         c+=1
#     i=i+1
# print(c)
# print(a)


# a="man,"
# b=5
# # c=a*b
# print(a*b)
# i=1
# while i<=10:
#     i=i+1
#     if i==4:
#         continue
#     print(i)


# a=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
# i=0
# max=0
# sum=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     if a[i]<0:
#         sum=sum+a[i]
#     i+=1
# print(max,"=",sum)



a=[10,5,20,10,30,10]
i=0
j=1
d=[]
while i<len(a):
    b=[]
    sub=a[i]-a[j]
    d.append(sub)
    i=i+2
    j=j+2
print(d)
