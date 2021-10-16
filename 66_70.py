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

#68번
n = int(input())
if n>=90:
    print('A')
elif n>=70:
    print('B')
elif n>=40:
    print('C')
else:
    print('D')

#69번
c = input()
if c=='A':
    print("best!!!")
elif c=='B':
    print("good!!")
elif c=='C':
    print("run!")
elif c=='D':
    print("slowly~")
else:
    print("what?")
    
#70번
n = int(input())
if n//3==1:
    print("spring")
elif n//3==2:
    print("summer")
elif n//3==3:
    print("fall")
else:
    print("winter")
