arr=eval(input("enter:"))
max_ones=0
count=0
for i in arr:
    if i==1:
        count=count+1
    else:
        count=0
    max_ones=max(count,max_ones)
print(max_ones)
