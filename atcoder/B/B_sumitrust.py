import math

n = int(input())

for i in range(1, 50000):
    if math.floor(i * 1.08) == n:
        print(i)
        exit()

print(":(")