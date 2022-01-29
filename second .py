# list=[1,2,4,5,18,19,20,60,50]
# i=0
# max=0
# sec=0
# while i<len(list):
#     if list[i]>max:
#         max=list[i]
#     i+=1
#     j=0
#     while j<len(list):
#         if max>list[j] and list[j]>sec:
#             sec=list[j]
#         j+=1
# print("first max number :-",max)
# print("sec max number :-",sec)


# list=[[2,3,4],[5,6,7,8],[4,5,9,2]]
# i=0
# b=[]
# sum=0
# row=0
# row1=0
# row2=0
# while i<len(list):
#     row=row+list[i][0]
#     row1=row1+list[i][1]
#     row2=row2+list[i][2]
#     i+=1
# print("total row",row)
# print("total row1",row1)
# print("total row2",row2)
# print("sum",row+row1+row2)


# list=[[2,3,4],[5,6,7,8],[4,5,9,2]]
# i=0
# sum=0
# b=[]
# sum=0
# sum1=0
# sum2=0
# while i<len(list):
#     sum=sum+list[i][0]
#     sum1=sum+list[i][1]
#     sum2=sum+list[i][2]
#     i+=1
# print("sum",[sum,sum1,sum2])
    
# list=[[2,3,4],[5,6,7,8],[4,5,9,2]]
# i=0
# b=[]
# while i<len(list):
#     j=0
#     sum=0
#     while j<len(list[i]):
#         sum=sum+list[i][j]
#         j+=1
# b.append(sum)
# i+=1

# a=[[2,3,4],[5,6,7,8],[4,5,9,2]]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j+=1
#     c.append(sum)
#     i+=1
# print(c)

# a=[4,5,6,[2,3,4],4,2,3]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)



i=1
k=1
while i<=9:
    j=1
    while j<=5:
        print(k,end=" ")
        j+=1
        k=k+2
    i+=2
    print()





