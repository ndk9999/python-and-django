#########################################################
# Luyen tap 06 - Bai 4 - Day bo ba so khong tao tam giac
#########################################################

import random
import math
import os
import shutil

min_values = [1,  1,  10,  100,   10**3, 10**6, 10**8, 10**10, 10**12, 10**14, 10**16]
max_values = [10, 50, 100, 10**3, 10**5, 10**7, 10**9, 10**11, 10**13, 10**15, 10**18]

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
    if n < 3 or k < 3:
        return 'NO'

    first = 1
    mid = 1
    count = 2

    while count < n and first + mid <= k:
        next = first + mid
        count += 1
        first = mid
        mid = next 

    if count < n:
        return 'NO'
    
    return 'YES'

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        k = random.randrange(min_values[i], max_values[i])
        n = random.randrange(min_values[i], max_values[i])

        if k < 10**3:
            n = random.randrange(1, 20)
        elif k < 10**6:
            n = random.randrange(5, 30)
        elif k < 10**9:
            n = random.randrange(10, 40)
        elif k < 10**12:
            n = random.randrange(15, 60)
        elif k < 10**15:
            n = random.randrange(20, 80)
        elif k < 10**18:
            n = random.randrange(25, 100)

        answer = solve(n, k)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n} {k}')
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

print(solve(1, 2))
print(solve(5, 5))
print(solve(3, 3))
print(solve(6, 5))
print(solve(87, 1000000000000000000))