S=str(input())

ans=True

#even
for i in range(1,len(S),2):
    if S[i].isupper():
        pass
    else:
        ans=False

#odd
for i in range(0,len(S),2):
    if S[i].islower():
        pass
    else:
        ans=False

if ans:
    print('Yes')
else:
    print('No')

