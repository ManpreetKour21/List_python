numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
l=[]
count=0
while i<len(numbers):
    x=numbers[i]
    if x>20 and x<40:
        l.append(x)
        count+=1
    i+=1
print("number above 20 and 40:-",l,"\n","how many count:-",count)
