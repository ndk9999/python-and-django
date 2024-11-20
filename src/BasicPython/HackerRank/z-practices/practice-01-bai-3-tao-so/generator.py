#########################################################
# Luyen tap 01 - Bai 3 - Tao so va tinh m + n
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  1,  1,  1,  1,     10,    10,    10,    10**2, 10**3, 10**4, 10**5]
max_values = [10, 20, 10, 10, 10**2, 10**2, 10**2, 10**6, 10**6, 10**6, 10**6, 10**6]

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

def solve(a, b, c):
    m = a * (10 ** len(str(b))) + b - a
    n = b * (10 ** len(str(c)))
    return m + n

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        b = randrange(10 ** randrange(1, 6) if i > 6 else min_values[i], max_values[i])
        c = randrange(10 ** randrange(1, 6) if i > 6 else min_values[i], max_values[i])
        s = solve(a, b, c)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(a), '\n', str(b), '\n', str(c)])
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