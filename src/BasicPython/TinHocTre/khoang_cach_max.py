n = int(input())
dayso = []

for _ in range(n):
    so = int(input())
    dayso.append(so)

dayso.sort()
#dayso.sort(reverse = True)

cd = len(dayso)
nho = dayso[0]
lon = dayso[cd - 1]
kc = lon - nho

a = dayso[::-1]

print(dayso)
print(a)
print(kc)
