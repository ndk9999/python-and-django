###################################################
# Thanh Pho Da Nang - 2024 - Bai 2 - Chu So Cuoi Cung
###################################################

from random import randrange
import os
import shutil

min_values = [0, 0,   0,     0,     0,     10**2, 10**2, 10**4, 10**4, 10**6, 10**6,  10**6]
max_values = [10, 20, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**10]

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
    dv = [1, 7, 9, 3]
    return dv[n % len(dv)]

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

# 108452 YES
# 212523 YES
# 52576148 YES
# 502705804830 YES
# 5642003329652 YES
# 17862943368599124 YES

