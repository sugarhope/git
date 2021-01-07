n, m, t = map(int, input().split())
battery = n
start = 0
for i in range(m):
  a, b = map(int, input().split())
  battery = battery - (a - start)
  if battery <= 0:
    print("No")
    break
  if battery + (b - a) > n:
    battery = n
  else:
    battery = battery + (b - a)
  if i == m-1:
    if battery - (t - b) <= 0:
      print("No")
    else:
      print("Yes")
  start = b