N=int(input())
A=list(map(int,input().split()))

B=sorted(A)
ans=[]
L=N
for i in range(0,N):
    temp=B[i]*L
    ans.append(temp)
    if i != len(B)-1 and B[i] != B[i+1]:
        L=N-i-1

print(max(ans))