n = 8
i = 0
j = 0
dem = 0
cot = [-1, -1, -1, -1, -1, -1, -1, -1]
hang = [False] * n
chinh = [False] * n * 2
phu = [False] * n * 2

while j >= 0:
    i = cot[j] + 1
    while i < n and (hang[i] == True or chinh[i - j + n - 1] == True or phu[i + j] == True):
        i = i + 1

    if cot[j] >= 0:
        k = cot[j]
        hang[k] = False
        chinh[k - j + n - 1] = False
        phu[k + j] = False
    
    if i >= n:
        cot[j] = -1
        j = j - 1
    else:
        cot[j] = i
        hang[i] = True
        chinh[i - j + n - 1] = True
        phu[i + j] = True
        j = j + 1

    if j >= n:
        dem = dem + 1
        print(dem, ": ", [x + 1 for x in cot])
        j = j - 1
