import math

n = 100

#r = 6
#c = 7
#grid = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']

r = 4
c = 5
grid = ['O...O', '.....', '.O.O.', '.....']

origin = [0] * r * c
zero = []
one = []
cache = []

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'O':
            origin[i * c + j] = 2
        else:
            zero.append(i * c + j)

start = [k for k in origin]
cache.append(list(start))

i = 1
print(origin)
print(f'After {i} seconds', start)

while True:
    # plant bombs
    for k in zero:
        start[k] = 4
        
    zero.clear()
    one.clear()
        
    for k in range(r * c):
        if start[k] > 0:
            start[k] -= 1
        if start[k] == 0:
            zero.append(k)
        elif start[k] == 1:
            one.append(k)
    
    i += 1
    print(f'After {i} seconds - plant', start)
    
    x = -1
    for j in range(len(cache)):
        if cache[j] == start:
            x = j
        
    if x > -1:
        break
    else:
        cache.append(list(start))
        
    if i == n:
        break

    # bombs detonate
    for k in one:
        start[k] = 0
        if k - c >= 0:
            start[k-c] = 0
        if k + c < r * c:
            start[k+c] = 0
        if k % c > 0:
            start[k-1] = 0
        if k % c < c-1:
            start[k+1] = 0
            
    one.clear()
        
    for k in range(r * c):
        if start[k] > 0:
            start[k] -= 1
        if start[k] == 0:
            zero.append(k)
        elif start[k] == 1:
            one.append(k)
    
    i += 1
    print(f'After {i} seconds - detonate', start)
    
    x = -1
    for j in range(len(cache)):
        if cache[j] == start:
            x = j
        
    if x > -1:
        break
    else:
        cache.append(list(start))
        
    if i == n:
        break

print(cache)
print(x, i)
#print(start)
