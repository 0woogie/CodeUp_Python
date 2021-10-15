#66번
data = list(map(int, input().split()))

for i in data:
    if i%2==0:
        print("even")
    else:
        print("odd")
        
#67번
n = int(input())

if n<0:
  if n%2==0:
    print('A')
  else:
    print('B')
else:
  if n%2==0:
    print('C')
  else:
    print('D')
