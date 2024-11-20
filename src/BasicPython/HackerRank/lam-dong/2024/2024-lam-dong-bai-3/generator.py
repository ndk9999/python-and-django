#########################################################
# Tinh Lam Dong - 2024 - Bai 3 - Doi so thuc qua phan so
#########################################################

from random import randrange
import os
import shutil

min_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
max_values = [10, 100, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11]

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

def ucln(a, b):
    if a == 0 or b == 0:
        return 1
    
    while b > 0:
        r = a % b
        a = b
        b = r

    return a

def solve(r):
    k = len(r) - 1
    mau = 1

    while k >= 0 and r[k] != '.':
        mau *= 10
        k -= 1
    
    r = r.replace('.', '')
    tu = int(r)
    uc = ucln(tu, mau)

    return tu // uc, mau // uc

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        p = randrange(min_values[i], max_values[i])
        c = randrange(0, 1000)

        # try to set numerator and denominator to 0 in some cases
        if c < 6:
            n = 0
        elif c > 994:
            p = 0

        r = f'{n}.{p}'
        s, v = solve(r)

        print(r, s, v)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(r)
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{s} {v}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()