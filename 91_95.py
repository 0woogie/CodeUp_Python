#91번
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)

#92번
n = int(input())
a = input().split()
for i in range(n):
  a[i] = int(a[i])
d = []
for i in range(24):
  d.append(0)
for i in range(n):
  d[a[i]] += 1
for i in range(1, 24):
  print(d[i], end=' ')

#93번
n = int(input())
a = input().split()
for i in range(n):
  a[i] = int(a[i])
for i in range(n-1, -1, -1):
  print(a[i], end=' ')

#94번
n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[0])

#95번
d = [[0]*20 for _ in range(20)]
n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  d[x][y] = 1
for i in range(1, 20):
  for j in range(1, 20): 
    print(d[i][j], end=' ')
  print()
