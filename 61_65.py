#61번
a, b = input().split()
a = int(a)
b = int(b)
print(a | b)

#62번
a, b = input().split()
a = int(a)
b = int(b)
print(a ^ b)

#63번
a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b)
print(c)

#64번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a<b:
    if c<a:
        print(c)
    else:
        print(a)
else:
    if c<b:
        print(c)
    else:
        print(b)

#65번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2==0 :
  print(a)
  
if b%2==0 :
  print(b) 
  
if c%2==0 :
  print(c)
