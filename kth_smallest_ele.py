#find kth smallest element of list
import heapq
def find_ksmall(arr):
    heapq.heapify(arr)
    while k>0:
        s=heapq.heappop(arr)
        k=k-1
    return s
arr=list(map(int,input("enter:").split()))
k=int(input("enter values:"))
ans=find_ksmall(arr,k)
print(ans)
