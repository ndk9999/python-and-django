#########################################################
# Luyen tap 05 - Bai 1 - Bat cap so cung tinh chan le
#########################################################

import random
import math
import os
import shutil

min_values = [1,  1,  1,  20, 10,  10**2, 10**3, 10**4, 10,    10**2,  10**3,  10**4]
max_values = [10, 20, 10, 50, 100, 10**3, 10**4, 10**5, 10**2, 10**3,  10**4,  10**5]

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

def solve(n, numbers):
    if n == 1:
        return numbers[0]

    odd = sum([x % 2 for x in numbers])

    return -1 if odd % 2 == 1 else sum(numbers)

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        m = min_values[i] * 10 if i < 5 else 10**6
        n = random.randrange(min_values[i], max_values[i])
        numbers = [random.randrange(0, m) for _ in range(n)]

        r = solve(n, numbers)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}\n')
        fi.write(' '.join([str(x) for x in numbers]))
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve(3, [1, 2, 3]))
print(solve(5, [1, 2, 3, 4, 5]))