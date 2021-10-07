#41번
a, b = input().split()
print(int(a)%int(b))

#42번
f = float(input())
print(round(f,2))

#43번
f1, f2 = input().split()
print(format(float(f1)/float(f2), ".3f"))

#44번
n, m = input().split()
a = int(n)
b = int(m)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

#45번
a, b, c = input().split()
sum = int(a) + int(b) + int(c)
avg = sum/3
print(sum, format(avg, ".2f"))
