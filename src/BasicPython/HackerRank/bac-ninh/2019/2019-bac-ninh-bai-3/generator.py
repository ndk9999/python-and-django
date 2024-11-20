#########################################################
# TP Bac Ninh - 2019 - Bai 3 - Day so
#########################################################

from random import randrange
import os
import shutil
import math

min_values = [1,  1, -10, -100, 100,   100,  1000,  10000,  100000,  100000,  1000000,  1000000]
max_values = [20, 50, 100, 1000, 10000, 1000, 10000, 100000, 1000000, 1000000, 10000000, 10000000]

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

def solve(m, n):
    if m <= 0 or n <= 0 or m >= 10**9 or n >= 10**9:
        return 0, 0

    so_thu_n = (n - 1) * (n - 1) + 1
    vt_be = int(math.sqrt(m - 1))
    so_be = vt_be * vt_be + 1
    so_lon = (vt_be + 1) * (vt_be + 1) + 1
    so_gan_m = so_be if m - so_be < so_lon - m else so_lon

    return so_thu_n, so_gan_m

def generate():
    for i in range(len(min_values)):
        m = randrange(min_values[i], max_values[i])
        n = randrange(min_values[i], max_values[i])

        p, q = solve(m, n)
        print(m , n , p, q)
        
        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{m} {n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{p} {q}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

#print(solve(943629, 943629))