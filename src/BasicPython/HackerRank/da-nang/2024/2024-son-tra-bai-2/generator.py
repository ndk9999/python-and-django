##############  #####################################
# Quan Son Tra - Da Nang - 2024 - Bai 2 - Hoan Doi
###################################################

from random import *
import os
import shutil
import string

min_values = [1,  5,  10, 10,  20,  50,  100, 200, 300, 400, 500, 700]
max_values = [10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 1000]

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

def solve(s, a, b):
    if a == b:
        return s
    
    t = list(s)
    t[a-1], t[b-1] = t[b-1], t[a-1]

    return ''.join(t)

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase, k=n))

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        s = rand_string(n)
        a = randrange(0, n)
        b = randrange(a, n)
        r = solve(s, a, b)

        print(f'{s} {a} {b} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([s, '\n', str(a), '\n', str(b)])
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(r)
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve('quansontra', 6, 10))
