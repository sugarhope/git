N=int(input())

buy=[]
for i in range(N):
    A,P,X=map(int,input().split())
    stock=X-(0.5+A-1+0.5)
    if stock>=1:
        buy.append(P)

if buy==[]:
    print(-1)
else:
    print(min(buy))