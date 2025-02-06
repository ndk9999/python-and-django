#########################################################
# Luyen tap 06 - Bai 2 - Dem so lan gap giay
#########################################################

import random
import math
import os
import shutil

min_values = [1,  20,  10,  100,   10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**5]
max_values = [20, 100, 100, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**9]

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

def solve(a, b):
    if a == b:
        return 0

    if a < b:
        a, b = b, a

    counter = 0
    r = a % b

    while r > 0:
        counter += a // b
        a = b
        b = r
        r = a % b

    if a > b:
        counter += a // b
        counter -= 1

    return counter

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        d = random.randrange(min_values[i], max_values[i])
        r = random.randrange(1, d)

        answer = solve(d, r)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{d} {r}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{answer}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve(10, 7))
print(solve(10, 2))