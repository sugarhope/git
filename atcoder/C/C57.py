n=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors
ans=[]
for A in make_divisors(n):
    temp=n/A
    if temp.is_integer():
        B=int(temp)
    ans.append(max(len(str(A)),len(str(B))))
print(min(ans))

