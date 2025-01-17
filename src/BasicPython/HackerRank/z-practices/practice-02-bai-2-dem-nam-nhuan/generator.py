#########################################################
# Luyen tap 02 - Bai 2 - Dem so nam nhuan giua 2 nam
#########################################################

from random import randrange
import os
import shutil

min_values = [2000, 1990, 0,    1000, 2000, 3000, 4000, 0,    1000, 2000, 3000, 4000]
max_values = [2150, 2025, 2000, 3000, 4000, 5000, 6000, 4000, 5000, 6000, 7000, 10000]

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

def is_leap_year(n):
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)

def solve(m, n):
    years = []
    m += 1

    while m < n:
        if is_leap_year(m):
            years.append(m)
        m += 1
    
    return years

def generate():
    for i in range(len(min_values)):
        m = randrange(min_values[i], max_values[i] - 1)
        n = randrange(m, max_values[i])
        r = solve(m, n)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{m} {n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{len(r)}\n')

        if len(r) > 0:
            fo.write(" ".join(map(str,r)))

        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()