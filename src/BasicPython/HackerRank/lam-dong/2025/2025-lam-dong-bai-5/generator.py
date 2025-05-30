#########################################################
# Tinh Lam Dong - 2024 - Bai 4 - Cap so dac biet
#########################################################

from random import *
import os
import shutil

min_values = [1,  1,  1,     10**2, 10**3, 10**4, 10**5, 10**6, 10**6, 10**7, 10**8, 10**9]
max_values = [10, 10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**7, 10**8, 10**9, 10**10]

working_dir = os.path.dirname(os.path.realpath(__file__))
problem_name = os.path.split(working_dir)[-1]
zip_file_path = os.path.join(working_dir, 'zipped-files')
test_case_path = os.path.join(working_dir, 'test-cases')
input_path = os.path.join(test_case_path, 'input')
output_path = os.path.join(test_case_path, 'output')

def create_folders():
    if not os.path.exists(zip_file_path):
        os.makedirs(zip_file_path)

    if not os.path.exists(test_case_path):
        os.makedirs(test_case_path)

    if not os.path.exists(input_path):
        os.makedirs(input_path)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

def solve(a, n):
    ds = []
    
    kq = a
    m = n
    b = a
    k = b % 10
    vt = 0

    while k > 0 and m > 0:
        if k % 2 == 0:
            b = (b + k * 2) % 1000
        else:
            b = (b * k) % 1000
        
        m -= 1
        k = b % 10

        if b in ds:
            vt = ds.index(b)
            break
        else:
            kq = b
            ds.append(b)

        if k == 1:
            break

    kt = len(ds)
    
    if kt > 0 and m >= 0 and k != 1:
        kt -= vt
        k = (n - vt - 1) % kt
        kq = ds[vt + k]

    return kq % 1000

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        n = randrange(min_values[i], max_values[i])
        r = solve(a, n)

        print(a, n, r)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{a}\n{n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(str(r))
        fo.close()

def generate2():
    for i in range(100):
        p = i % 10 + 2
        a = randrange(min_values[p], max_values[p])
        n = randrange(min_values[p], max_values[p])
        r = solve(a, n)
        print(f'{a} {n} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau5.inp'), mode='w')
        fi.write(f'{a}\n{n}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau5.out'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

        i += 1

    shutil.make_archive(
        os.path.join(zip_file_path, problem_name + '_test_cases'), 
        'zip', 
        os.path.join(working_dir, 'samples'))

def zip_files():
    shutil.make_archive(os.path.join(zip_file_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
# generate2()
zip_files()

print(0  , solve(1123, 0))
print(1  , solve(1123, 1))
print(2  , solve(1123, 2))
print(3  , solve(1123, 3))
print(4  , solve(1123, 4))
print(5  , solve(1123, 5))
print(99 , solve(1123, 99))
print(100, solve(1123, 100))
print(101, solve(1123, 101))
print(102, solve(1123, 102))
print(103, solve(1123, 103))
print(104, solve(1123, 104))
print(105, solve(1123, 105))
