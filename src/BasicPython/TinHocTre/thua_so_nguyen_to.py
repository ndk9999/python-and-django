import time

cache = [0] * 5000001

def chain(n):
    if n == 1:
        return 1
        
    if n < 5000001 and cache[n] > 0:
        return cache[n]
        
    m = n // 2 if n % 2 == 0 else n * 3 + 1
    
    c = chain(m) + 1
    
    if n < 5000001:
        cache[n] = c
        
    return c

def find_max(n):
    m = 0
    r = 0
    
    for j in range(1, n + 1):
        k = chain(j)
        if m <= k:
            m = k
            r = j
            
    return r
    
start_time = time.time()
    
#print(chain(20))
print(find_max(5000000))

print("--- %s seconds ---" % (time.time() - start_time))

#for i in range(1, 1001):
#    print(i, chain(i))
