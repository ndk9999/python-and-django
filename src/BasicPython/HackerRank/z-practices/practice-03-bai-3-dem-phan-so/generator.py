#########################################################
# Luyen tap 03 - Bai 3 - Dem phan so
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  1,  0,  10,    10**2, 0,     10**2, 0,  10,    10**2, 0,     10**2]
max_values = [10, 20, 10, 10**2, 10**3, 10**2, 10**3, 10, 10**2, 10**3, 5, 10**3]

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
    if a == b and b == c:
        if a == 0:
            return 0
        else:
            return 1
    elif a == b:
        if a == 0 or c == 0:
            return 2
        else:
            return 4
    elif a == c:
        if a == 0 or b == 0:
            return 2
        else:
            return 4
    elif c == b:
        if c == 0 or a == 0:
            return 2
        else:
            return 4
    elif a == 0 or b == 0 or c == 0:
        return 6
    else:
        return 9

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        b = randrange(min_values[i], max_values[i])
        c = randrange(min_values[i], max_values[i])

        r = solve(a, b, c)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{a}\n{b}\n{c}\n')
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

print(0, 0, 0, solve(0, 0, 0))
print(1, 1, 1, solve(1, 1, 1))
print(0, 0, 1, solve(0, 0, 1))
print(1, 1, 0, solve(1, 1, 0))
print(1, 1, 2, solve(1, 1, 2))
print(0, 1, 2, solve(0, 1, 2))
print(3, 1, 2, solve(3, 1, 2))