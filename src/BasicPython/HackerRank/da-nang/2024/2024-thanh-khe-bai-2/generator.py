###################################################
# Thanh Khe - Da Nang - 2024 - Bai 2 - Hoi Khoe Phu Dong
###################################################

from random import *
import os
import shutil
import string

min_values = [1,  1,  1,     10,    10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8,     10**9]
max_values = [15, 30, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 2 * 10**9, 2 * 10**9]

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

def solve(x, y, z):
    if y == 0 or z == 0 or y + z <= x:
        return 0

    return y + z - x

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase + string.digits, k=n))

def generate():
    for i in range(len(min_values)):
        x = randrange(min_values[i], max_values[i])
        y = randrange(min_values[i], x + 1)
        z = randrange(min_values[i], x + 1)
        r = solve(x, y, z)

        #print(f'{n} {mi} {ma}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{x} {y} {z}')
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

print(7, 3, 4, solve(7, 3, 4))
print(22, 15, 12, solve(22, 15, 12))