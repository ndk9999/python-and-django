#########################################################
# Tinh An Giang - 2021 - Bai 2 - Sap xep 4 so
#########################################################

from random import randrange
import os
import shutil

min_values = [0,  0,  0,  10,    10**2, 10**2, 10**3, 10**4, 0,     10**1, 10**2, 10**3]
max_values = [10, 20, 20, 10**2, 10**3, 10**4, 10**5, 10**6, 10**2, 10**3, 10**5, 10**6]

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

def solve(a, b, c, d):
    dem = 0

    if a < d:
        a, d = d, a
        dem += 1

    if b < c:
        b, c = c, b
        dem += 1

    if a < b:
        a, b = b, a
        dem += 1

    if c < d:
        c, d = d, c
        dem += 1

    if b < c:
        b, c = c, b
        dem += 1

    return dem, a, b, c, d

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        b = randrange(min_values[i], max_values[i])
        c = randrange(min_values[i], max_values[i])
        d = randrange(min_values[i], max_values[i])
        
        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(a), '\n', str(b), '\n', str(c), '\n', str(d)])
        fi.close()

        dem, a, b, c, d = solve(a, b, c, d)
        print(f'{dem} {a} {b} {c} {d}')

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.writelines([str(dem), '\n', f'{a} {b} {c} {d}'])
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()