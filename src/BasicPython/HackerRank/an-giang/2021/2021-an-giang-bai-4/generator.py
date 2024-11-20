###################################################
# Phu Tan - An Giang - 2021 - Bai 2 - Tong day so
###################################################

from random import randrange
import os
import shutil

min_values = [1, 1,  -10, -50,  -100,    10**2, 10**3, 10**5, 10**5, 10**6, 10**7, 10**7]
max_values = [10, 20, 10, 10**2, 10**3, 10**5, 10**5, 10**6, 10**9, 10**7, 10**8, 10**10]

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
    if n < 1 or n > 10 ** 8:
        return 0

    return 2 * n * (n + 1) - n

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        r = solve(n)

        print(f'{n} {r}')

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