# list1=[1,2,3,4,5,6,]
# list2=[1,2,3,6,]
# i=0
# list3=[]
# while i<len(list1):
#     if list1[i] not in list2:
#         print(list1[i])
#     i+=1

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# i=0
# list3=[]
# while i<len(list1):
# 	if list1[i] not in list2:
# 	    print(list1[i])
# 	i+=1

a=[4,2,3,5]
b=[3,5,1,8]
i=0
list1=[]
while i<len(a):
    if a[i] not in b:
        list1.append(a[i])
    i+=1
print(list1)    

