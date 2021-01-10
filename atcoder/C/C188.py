N=int(input())
A=list(map(int,input().split()))

AA=[[],[]]
for i in range(0,len(A)//2):
    AA[0].append(A[i])
for j in range(len(A)//2,len(A)):
    AA[1].append(A[j])
ans=min(max(AA[0]),max(AA[1]))
print(A.index(ans)+1)
