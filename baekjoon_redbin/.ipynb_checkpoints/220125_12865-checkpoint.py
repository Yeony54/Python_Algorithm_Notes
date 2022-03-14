n,k = list(map(int, input().split()))
bag = [0 for _ in range(k+1)]

for i in range(n):
    w,v = list(map(int, input().split()))
    for j in range(k,w-1,-1):
        if w <= j:
            bag[j] = max(bag[j],bag[j-w]+v)

print(bag[-1])