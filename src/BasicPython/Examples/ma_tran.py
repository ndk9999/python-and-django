# Ma nguon nay huong dan cach giai cac bai toan co ban tren ma tran
# Du lieu dau vao duoc doc tu tap tin matran.txt co cau truc nhu sau
# Dong dau tien chua 2 so m va n tuong ung voi so hang va so cot
# m dong tiep theo, moi dong chua n so nguyen


# ==============================================================
# DOAN MA SAU DAY HUONG DAN CACH DOC MA TRAN TU TAP TIN
# Chu y: mode='r' la mo tap tin de ghi du lieu vao tap tin

# Buoc 1. Mo file de doc
fi = open('D:\Projects\Mine\PythonAndDjango\src\BasicPython\Examples\matran.txt', mode='r')

# Buoc 2. Doc dong dau tien de lay gia tri m va n
data = fi.readline()
m, n = map(int, data.strip().split())

# Buoc 3. Khoi tao ma tran
mat = []

# Buoc 4. Doc cac phan tu cua ma tran
for i in range(m):
    # Doc het mot dong
    data = fi.readline()

    # Tach cac so trong dong do va chuyen thanh mang so
    row = list(map(int, data.strip().split()))

    # Them mang so vua doc duoc vao ma tran
    mat.append(row)

# Buoc 5. Dong tap tin
fi.close()


# ==============================================================
# XUAT MA TRAN DA DOC DUOC TU TAP TIN
print(f'So hang: {m}')
print(f'So cot : {n}')
print('Gia tri cac phan tu cua ma tran:')

for i in range(m):
    for j in range(n):
        print(f'{mat[i][j]}\t', end='')
    print('')


# ==============================================================
# TINH TONG CAC PHAN TU XUNG QUANH MA TRAN
# Y tuong: Tinh tong hang dau & cuoi, cot dau & cuoi

total = 0

# Duyet qua m hang, tinh tong cac so o cot dau va cot cuoi
for i in range(m):
    total += mat[i][0]
    total += mat[i][n-1]

# Duyet tu cot thu 2 den cot ke cuoi, tinh tong cac so tren
# hang dau tien va hang cuoi cung
for i in range(1, n-1):
    total += mat[0][j]
    total += mat[m-1][j]

# In ket qua ra man hinh
print(f'Tong xung quanh ma tran la: {total}')


# ==============================================================
# TIM VA XUAT 2 DUONG CHEO CUA MA TRAN VUONG RA TAP TIN
# THAO TAC NAY CHI AP DUNG CHO TRUONG HOP MA TRAN VUONG (m = n)
# Chu y: mode='w' la mo tap tin de ghi du lieu vao tap tin

# Buoc 1. Tao tap tin de ghi
fo = open('D:\Projects\Mine\PythonAndDjango\src\BasicPython\Examples\cheo.txt', mode='w')

# Buoc 2. Duyet qua cac so tren duong cheo chinh va ghi du lieu vao tap tin
for i in range(m):
    fo.write(f'{mat[i][i]} ')

# Xuong dong de ghi tiep duong cheo phu
fo.write('\n')

# Hoac dung cach sau
chinh = [str(mat[i][i]) for i in range(m)]
fo.write(" ".join(chinh))
fo.write('\n')

# Buoc 3. Duyet qua cac so tren duong cheo phu va ghi du lieu vao tap tin
for i in range(m):
    fo.write(f'{mat[i][n-i-1]} ')

# Xuong dong
fo.write('\n')

# Hoac dung cach sau
phu = [str(mat[i][n-i-1]) for i in range(m)]
fo.write(" ".join(phu))
fo.write('\n')

# Buoc 4. Dong tap tin
fo.close()


# ==============================================================
