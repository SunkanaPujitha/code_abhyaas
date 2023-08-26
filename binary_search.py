a=eval(input("enter:"))
b=sorted(a)
print(b)
num=int(input("enter a number:"))
n=len(a)
left=0
right=n-1
while(left<=right):
    mid=(left+right)//2
    if(b[mid]==num):
        print(num, "is found")
        break;
    if(b[mid]<num):
        left=mid+1
    else:
        right=mid-1
if(left>right):
    print(num,"is not found")
