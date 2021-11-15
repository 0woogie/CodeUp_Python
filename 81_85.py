#81번
n = int(input(), 16)
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
    
#82번
n = int(input())
for i in range(1, n+1):
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=' ')
    else:
        print(i, end=' ')
        
#83번
r, g, b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1   
print(count)

#84번
h, b, c, s = map(int, input().split())
result = h*b*c*s/8/1024/1024
print(round(result, 1), "MB")

#85번
w, h, b = map(int, input().split())
result = w*h*b/8/1024/1024
print("%0.2f MB" % result)
#print(round(result, 2), "MB") <--test case가 소수점 첫째 자리에서 끝나는 경우가 있어서 사용할 수 없었다.
