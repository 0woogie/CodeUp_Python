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
