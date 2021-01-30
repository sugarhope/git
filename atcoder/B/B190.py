N,S,D=map(int,input().split())
damage=False

for i in range(N):
    x,y=map(int,input().split())
    if x<S and y>D:
        damage=True

if damage:
    print('Yes')
else:
    print('No')