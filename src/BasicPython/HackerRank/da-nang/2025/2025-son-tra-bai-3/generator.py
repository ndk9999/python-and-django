###################################################
# Quan Son Tra - 2025 - Bai 3 - Hai Tao
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

def solve(m, n):
    if m * n == 0:
        return 'NO'

    if m > n:
        m, n = n, m

    if m % 2 == 1:
        return f'YES {m * 2 + 1}'
    elif n % 2 == 1:
        return f'YES {n * 2 + 1}'

    return 'NO'

def generate():
    for i in range(len(min_values)):
        m = randrange(min_values[i], max_values[i])
        n = randrange(min_values[i], max_values[i])
        r = solve(m, n)

        print(f'{m}, {n} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{m}\n{n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

def generate2():
    test_cases = [
        [2, 3],
        [2, 2],
        [13, 19],
        [74, 74],
        [228, 322],
        [1726, 1047],
        [64921529613544, 38495809656715],
        [758658, 802414],
        [3529084954, 53618849],
        [1555990614, 410001372],
        [625404591582, 624664192668],
        [168985887017115, 695041006122945],
    ]

    i = 0

    for [m, n] in test_cases:
        r = solve(m , n)

        print(f'{m} {n} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau3.inp'), mode='w')
        fi.write(f'{m}\n{n}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau3.out'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
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
# generate()
generate2()
# zip_files()

print(solve(2, 3))
print(solve(2, 2))
print(solve(0, 10))
print(solve(1001, 25))