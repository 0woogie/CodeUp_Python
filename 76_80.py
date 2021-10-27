#76번
n = int(input())
for i in range(n+1):
  print(i)
  
#77번
n = int(input())
sum = 0
for i in range(n+1) :
  if i%2==0:
    sum += i
print(sum)

#78번
while True:
     c = input()
     print(c)
     if c=='q':
          break

#79번
n = int(input())
sum = 0
x = 1
while True:
    sum += x
    if sum >= n:
        break
    x += 1
print(x)

#80번
n, m = map(int, input().split())
for i in range(1, n+1):
  for j in range(1, m+1):
    print(i, j)
