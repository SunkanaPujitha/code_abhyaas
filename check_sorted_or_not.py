arr=eval(input("enter:"))
j=arr[0]
for i in range(1,len(arr)):
    if(j<arr[i]):
        flag=1
        j=arr[i]
    else:
        flag=0
        break;
if(flag==1):
    print("array is in sorted order")
else:
    print("array is not in sorted order")
