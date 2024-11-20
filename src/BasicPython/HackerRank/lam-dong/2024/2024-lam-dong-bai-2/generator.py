#########################################################
# Tinh Lam Dong - 2024 - Bai 2 - So chia het cho 5
#########################################################

from random import randrange
import os
import shutil

min_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
max_values = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

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
    if a == 0 and b == 0 and c == 0:
        return 'NO'
    
    du = (a * b * c) % 5

    return 'YES' if du == 0 or du == 5 else 'NO'

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        b = randrange(min_values[i], max_values[i])
        c = randrange(min_values[i], max_values[i])
        r = solve(a, b, c)

        print(a, b, c, r)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(a), '\n', str(b), '\n', str(c)])
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(str(r))
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()