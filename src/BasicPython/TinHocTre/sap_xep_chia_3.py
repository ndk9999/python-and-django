n = int(input())
vt = 0
day_so = []

while vt < n:
    so = int(input())
    day_so.append(so)
    vt += 1

chia_het_3 = [x for x in day_so if x % 3 == 0]
chia_3_du_1 = [x for x in day_so if x % 3 == 1]
chia_3_du_2 = [x for x in day_so if x % 3 == 2]

chia_het_3.sort(reverse = True)
chia_3_du_1.sort()
chia_3_du_2.sort(reverse = True)

print(day_so)
print(chia_het_3)
print(chia_3_du_1)
print(chia_3_du_2)
