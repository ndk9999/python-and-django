#########################################################
# Tinh Tien Giang - 2020 - Bai 2 - Tim phan tu cua day so
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  5,  11,  101, 1001, 5001,  -100, 10001, 50001, 75001, 100001,  1000000]
max_values = [10, 20, 500, 500, 5000, 10000, 0,    50000, 75000, 100000, 1000000, 10000000]

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

def solve(n):
    if n < 0 or n >= 10000000:
        return 0
    
    kc = n // 2 + 1 if n % 2 == 0 else (n + 1) // 2 + 1
    so = kc * (kc + 1) - 2

    return so if n % 2 == 0 else so - kc

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        r = solve(n)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(str(n))
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