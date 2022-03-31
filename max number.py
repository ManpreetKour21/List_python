numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i+=1
print(max)


# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# max=0
# sec=0
# while i<len(numbers):
#     if numbers[i]>max:
#         max=numbers[i]
#     i+=1
#     j=0
#     while j<len(numbers):
#         if max>numbers[j] and numbers[j]>sec:
#             sec=numbers[j]
#         j=j+1
# print(max)
# print(sec)


# 1
# list1=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# list1=[[0],[1,2,3],[6,7,8,10,11],[23,24]]
# i=0
# max=0
# while i<len(list1):
#     count=0
#     j=0
#  while j<len(list1[i]):
#         count=count+1
#         if count>max:
#             max=count
#             li=list1[i]
#         j=j+1
#     i=i+1
#     # print(count)
# print("max length =",max,"it's list-",li)


