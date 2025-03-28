###################################################
# Quan Son Tra - 2025 - Bai 2 - Trang Sach
###################################################

from random import randrange
import os
import shutil

min_values = [1, 1,   10**0, 10**2, 10**3, 10**4, 10**5, 10**6, 10**8,  10**10, 10**12, 10**14]
max_values = [10, 20, 10**2, 10**3, 10**4, 10**5, 10**6, 10**8, 10**10, 10**12, 10**14, 10**15]

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

def solve(n, k):
    p = n // k
    d = n % k

    if d > 0:
        p += 1
    else:
        d = k

    return p, d

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        k = randrange(1, min(10 ** 5, n + 1))
        x, y = solve(n, k)

        print(f'{k}, {n} {x} {y}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}\n{k}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{x} {y}')
        fo.close()

def generate2():
    test_cases = [
        [3, 10],
        [25, 45],
        [18, 84],
        [47, 301],
        [1729, 1927],
        [7136, 78025],
        [678954, 678954],
        [4058, 5064384],
        [63924, 7367451250],
        [1, 789309220344],
        [94650, 88918353209100],
        [28518, 449061522378796],
    ]

    i = 0

    for [k, n] in test_cases:
        x, y = solve(n, k)

        print(f'{k} {n} {x} {y}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau1.inp'), mode='w')
        fi.write(f'{k}\n{n}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau1.out'), mode='w', encoding='utf-8')
        fo.write(f'{x} {y}')
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

print(solve(100, 10))
print(solve(17, 1))
print(solve(10, 3))
print(solve(7, 25))