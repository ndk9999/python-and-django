n = int(input())

kq = 0
nua = n // 2

if n > 2:
    m = 2
    
    while m * (m + 2) <= n:
        m += 1

    # khuc dau
    if m < nua:
        kq = m * (m - 1) // 2

    # khuc cuoi
    kq += nua + n % 2

    if nua < 2:
        kq -= 1

    # khuc giua
    m += 1
    while m < nua:
        k = n // m
        
        if k * (m + 1) > n:
            k -= 1

        r = n - (m + 1) * k
        t = r // k + 1

        kq += k * t
        m += t

print(kq)
    

dem = 0
cap = []

for b in range(1, n + 1):
   for a in range(b + 1, n + 1):
       if a // b == a % b:
           cap.append((a, b))
           dem += 1

sorted(cap, key = lambda tup: tup[1])

for x in cap:
   print(x[0], x[1])

print(dem)
