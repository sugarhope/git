X=str(input())
M=int(input())

d=''.join(sorted(str(X), reverse = True))
d=d[0]
d=int(d)

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out

count = 0

for i in range(d+1, 10000):

    if i==1:
        pass

    else:
        temp = Base_n_to_10(X,i)
        if temp <= M:
            count += 1

print(count)