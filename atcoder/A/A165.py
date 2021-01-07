K=int(input())
A,B=map(int,input().split())

ans=''
for i in range(A,B+1):
    if i % K == 0:
        ans = 'OK'
        print(i)
if ans != 'OK':
    ans = 'NG'
print(ans)