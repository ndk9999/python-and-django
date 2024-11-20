#########################################################
# Hoa Vang - Da Nang - 2024 - Bai 2 - Ghep so
#########################################################

import random
import os
import shutil

min_values = [1,  2,  1, 10,  100, 500,  1000, 2000, 3000, 4000, 5000, 6000]
max_values = [6, 10, 10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 10000]

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
    numbers = [0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999]
    return numbers[n]

def generate():
    numbers = [2, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    for i in range(len(numbers)):
        n = numbers[i]
        s = solve(n)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{s}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve(2))
print(solve(5))