def subarr(arr,N,K):
    maxlength = 0
    for i in range(0,N):
        sum=0
        for j in range(i,N):
            sum=sum+arr[j]
            if sum==K:
                maxlength=max(maxlength, j - i + 1)
    return maxlength
arr= eval(input("enter arr:"))
N = len(arr)
K = int(input("enter sum:"))
print("length=", subarr(arr,N,K))
