#########################################################
# Luyen tap 04 - Bai 3 - So may man va gan may man
#########################################################

import random
import math
import os
import shutil

min_values = [1,  1,  1,   100,   10**3,  10**4,  0,    100,    10**3,  10**4,  10**2,  10**3]
max_values = [10, 50, 100, 10**3, 10**4,  10**5,  100,  10**3,  10**4,  10**5,  10**4,  10**5]

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

def lucky(n):
    if n < 2:
        return 'NO'
    
    while n > 0:
        r = n % 10
        if r != 2 and r != 5:
            return 'NO'
        n = n // 10

    return 'YES'

def almost_lucky(n):
    if n < 2:
        return 'NO'
    
    return 'YES' if n % 2 == 0 or n % 5 == 0 else 'NO'

def solve(numbers):
    return [almost_lucky(x) for x in numbers]

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        n = random.randrange(min_values[i], max_values[i])
        mv = 0

        if n <= 10:
            mv = 100
        elif n <= 100:
            mv = 10**3
        elif n <= 1000: 
            mv = 10**4
        elif n <= 10000:
            mv = 10**5
        else:
            mv = 10**6

        numbers = [random.randint(0, mv) for _ in range(n)]

        r = solve(numbers)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(' '.join([str(x) for x in numbers]))
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(' '.join([x for x in r]))
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))