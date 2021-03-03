S=list(str(input()))

a=S.count('a')
b=S.count('b')
c=S.count('c')
mvote=max(a,b,c)

if a==mvote:
    print('a')
elif b==mvote:
    print('b')
elif c==mvote:
    print('c')