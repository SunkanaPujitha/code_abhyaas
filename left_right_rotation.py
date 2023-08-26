def reverse (arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
arr=eval(input("enter a array:"))
n=len(arr)
d=int(input("enter:"))
#left shift of d positions
reverse (arr,0,d-1)
reverse (arr,d,n-1)
reverse (arr,0,n-1)
print(arr)



# right rotation

def reverse (arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
arr=eval(input("enter a array:"))
n=len(arr)
d=int(input("enter:"))
reverse (arr, 0, n-d-1)
reverse (arr,n-d,n-1)
reverse (arr, 0,n-1)
print(arr)
