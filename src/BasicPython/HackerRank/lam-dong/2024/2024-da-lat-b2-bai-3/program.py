import os

working_dir = os.path.dirname(os.path.realpath(__file__))

fi = open(os.path.join(working_dir, 'bfor002.inp'), 'r')
n, k, b = map(int, fi.readline().strip().split())
day = []

for i in range(0, n):
    so = int(fi.readline().strip())
    day.append(so)

fi.close()

tong = sum(day)
dau = (b - 1) % n
luot = k // n
le = k % n

print(dau, luot, le)

ketqua = tong * luot

for i in range(0, le):
    ketqua += day[(dau + i) % n]

fo = open(os.path.join(working_dir, 'bfor002.out'), 'w')
fo.write(str(ketqua))
fo.close()
