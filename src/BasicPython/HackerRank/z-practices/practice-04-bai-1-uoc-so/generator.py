#########################################################
# Luyen tap 04 - Bai 1 - Tim tat ca uoc so cua N
#########################################################

from random import randrange
import math
import os
import shutil

min_values = [1,  1,  1,   10,    10**2,  10**3,  10**4,  10**5,  10**6,  10**7,  10**8,   10**10]
max_values = [20, 50, 100, 10**3, 10**4,  10**5,  10**6,  10**7,  10**8,  10**9,  10**10,  10**12]

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
    divisors = []
    m = int(math.sqrt(n))

    for i in range(1, m+1):
        if n % i > 0:
            continue

        divisors.append(i)

        if i * i != n:
            divisors.append(n // i)

    return sorted(divisors)

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        r = solve(n)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(' '.join([str(x) for x in r]))
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve(0))