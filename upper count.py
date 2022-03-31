string=("AmeESHA")
i=0
b=[]
while i<len("AmeESHA"):
    if string[i]==string[i].lower():
        b.append(i)
    i+=1
print(b)