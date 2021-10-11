#56번
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#57번
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or ((not c) and (not d)))

#58번
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((not c) and (not d))

#59번
a=int(input())
print(~a)

#60번
a, b = input().split()
a = int(a)
b = int(b)
print(a & b)
