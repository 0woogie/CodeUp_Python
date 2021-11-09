#86번
n = int(input())
sum = 0
count = 0
while True :
  sum += count
  count += 1
  if sum>=n :
    break
print(sum)

#87번
n = int(input())
for i in range(1, n+1) :
  if i%3==0:
    continue
  print(i, end=' ')

#88번
a, d, n = map(int, input().split())
result = a + d*(n-1)
print(result)

#89번
a, r, n = map(int, input().split())
result = a
for _ in range(n-1):
    result *= r
print(result)

#90번
