#########################################################
# Luyen tap 03 - Bai 3 - Dem phan so
#########################################################

from random import randrange
import os
import shutil
import math

min_values = [1,  1,  0,  1,  10,    10,    10**2, 10**2, 10**3, 10**3, 10**4, 10**5]
max_values = [10, 20, 10, 50, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9]

working_dir = os.path.dirname(os.path.realpath(__file__))
problem_name = os.path.split(working_dir)[-1]
test_case_path = os.path.join(working_dir, 'test-cases')
input_path = os.path.join(test_case_path, 'input')
output_path = os.path.join(test_case_path, 'output')

def create_folders():
    if not os.path.exists(test_case_path):
        os.makedirs(test_case_path)

    if not os.path.exists(input_path):
        os.makedirs(input_path)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

def ucln(x, y):
    if x == 0 or y == 0:
        return 1
    return math.gcd(x, y)

def reduce(x, y):
    uc = ucln(x, y)
    return x // uc, y // uc

def generate_divisors(n):
    divisors = []
    mid = int(math.sqrt(n)) + 1

    for i in range(1, mid):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)

    return divisors

def solve(n, m , c, x, y):
    # Du lieu dau vao sai
    if n <= 0 or m < 0 or c < 0 or x < 0 or y < 0 or n > 10**9 or m > 10**9 or c > 10**9 or x > 10**9 or y > 10**9:
        return -1
    
    # Du lieu sai: cac truong hop khac
    if m > n or c > m or x > y or (x == 0 and c > 0):
        return -1
    
    # Khong can lam dung cau nao
    if x == 0 and c == 0:
        return 0

    # Khong the co phuong an
    if x * n % y > 0:
        return -1

    # Tong so cau dung
    scd = x * n // y

    # Da lam het n cau hoi (m == n)
    if m == n:
        if scd == c:
            return 0
        else:
            return -1

    # Neu tong so cau dung can lon hon n hoac nho hon c
    # hoac so cau dung can lam lon hon so cau hoi con lai
    if scd > n or scd < c or scd - c > n - m:
        return -1
    
    return scd - c

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        m = randrange(1, max(2, n))
        c = randrange(0, m)

        x = randrange(min_values[i], max_values[i])
        divisors = generate_divisors(x * n)
        divisors = [k for k in divisors if k >= x]
        y = divisors[randrange(0, len(divisors))]

        print(n, m, c, x, y)

        x, y = reduce(x, y)
        r = solve(n, m, c, x, y)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n} {m} {c} {x} {y}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

# create_folders()
# generate()
zip_files()

print(10, 6, 3, 1, 2, ' : ', solve(10, 6, 3, 1, 2))