###################################################
# Quan Son Tra - 2025 - Bai 1 - Dien Tich
###################################################

from random import randrange
import os
import shutil

min_values = [0, 0,   10**0, 10**1, 10**2, 10**3, 10**4, 10**1, 10**2, 10**3, 10**4, 10**5]
max_values = [10, 20, 10**2, 10**3, 10**4, 10**5, 10**6, 10**2, 10**3, 10**4, 10**5, 10**6]

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

def solve(n, a, b):
    if (a == 0 and b == 0) or n == 0:
        return 0
    
    dthv = n * n
    dta = (a * b) / 2
    dtb = (n * (n - a)) / 2
    dtc = (n * (n - b)) / 2

    return round(dthv - dta - dtb - dtc, 2)

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        a = randrange(0, n + 1)
        b = randrange(0, n + 1)
        r = solve(n, a, b)

        print(f'{n} {a} {b} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}\n{a}\n{b}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(str(r))
        fo.close()

def generate2():
    test_cases = [
        [100, 10, 10],
        [20, 3, 5],
        [8, 7, 3],
        [89, 47, 18],
        [30, 3, 1],
        [263, 263, 263],
        [335, 195, 275],
        [3, 3, 3],
        [1415, 1351, 419],
        [12379, 9521, 3008],
        [788929, 39995, 290804],
        [571510, 363939, 454717]
    ]

    i = 0

    for [n, a, b] in test_cases:
        r = solve(n, a, b)

        print(f'{n} {a} {b} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau1.inp'), mode='w')
        fi.write(f'{n}\n{a}\n{b}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau1.out'), mode='w', encoding='utf-8')
        fo.write(str(r))
        fo.close()

        i += 1

    shutil.make_archive(
        os.path.join(test_case_path, problem_name + '_test_cases'), 
        'zip', 
        os.path.join(working_dir, 'samples'))

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
generate2()
zip_files()

print(solve(100, 10, 10))
print(solve(5, 1, 5))