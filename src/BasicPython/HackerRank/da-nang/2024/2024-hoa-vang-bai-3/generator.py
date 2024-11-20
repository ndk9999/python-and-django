###################################################
# Hoa Vang - Da Nang - 2024 - Bai 2 - Chu So Tan Cung
###################################################

from random import randrange
from random import choices
import os
import shutil
import string

min_values = [1, 1,   1,  10, 10,    10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8]
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

def solve(n, d):
    du = (n - d) % 10
    cuoi = n - du
    m = (cuoi - d) // 10 + 1

    return (d + cuoi) * m // 2

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase + string.digits, k=n))

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        d = randrange(0, 10)
        r = solve(n, d)

        print(f'{n} {d} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n} {d}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(str(r))
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve(50, 1))