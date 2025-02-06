#########################################################
# Luyen tap 05 - Bai 2 - Chiec hop dieu ky
#########################################################

import random
import math
import os
import shutil

min_values = [1,  20,  10,  100,   10**3, 10**4, 10**5, 10**1,  10**2,  10**4, 10**3]
max_values = [20, 100, 100, 10**3, 10**4, 10**5, 10**6, 10**3,  10**4,  10**6, 10**6]

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

def solve(teo, tun):
    n = len(teo)
    d = sum([teo[i] != tun[i] for i in range(n)])

    return d // 2 if d % 2 == 0 else -1

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        n = random.randrange(min_values[i], max_values[i])
        teo = ''.join(random.choices('01', k=n))
        tun = ''.join(random.choices('01', k=n))

        answer = solve(teo, tun)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{teo}\n{tun}')
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

print(solve('00110', '10100'))
print(solve('0011000111', '1010010001'))