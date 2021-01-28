N,M=map(int,input().split())

temp=[0]*N
ss=[]
sc=[]

for _ in range(M):
    s,c=map(int,input().split())
    if s==1 and c==0 and N!=1:
        print(-1)
        exit()
    else:
        if s not in ss:
            temp[s-1]=c
        elif s in ss and [s,c] in sc:
            temp[s-1]=c
        elif s in ss and [s,c] not in sc:
            print(-1)
            exit()
    sc.append([s,c])
    ss.append(s)


if temp[0]==0 and N!=1:
    temp[0]=1

if N==3:
    print(100*temp[0]+10*temp[1]+temp[2])
elif N==2:
    print(10*temp[0]+temp[1])
else:
    print(temp[0])