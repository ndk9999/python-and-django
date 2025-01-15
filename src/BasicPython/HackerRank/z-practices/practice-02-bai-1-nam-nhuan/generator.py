#########################################################
# Luyen tap 01 - Bai 1 - Boc bi
#########################################################

from random import randrange
import os
import shutil

min_values = [2024, 2100, -100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 10000]
max_values = [2025, 2101, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9999, 12000]

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
    if n <= 0 or n > 9999:
        return 'INVALID'
    elif n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        return 'YES'
    else:
        return 'NO'

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        r = solve(n)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}')
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