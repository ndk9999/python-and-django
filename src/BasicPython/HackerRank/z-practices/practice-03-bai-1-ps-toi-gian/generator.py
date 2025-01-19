#########################################################
# Luyen tap 03 - Bai 1 - Toi gian phan so
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  1,  0,  10,    10**1, 10**2, 10**3, 10**4, 10**6, 10**8,  10**2, 10**6]
max_values = [10, 20, 10, 10**2, 10**3, 10**4, 10**5, 10**7, 10**9, 10**10, 10**5, 10**10]

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

def ucln(x, y):
    x = abs(x)
    y = abs(y)

    if x == 0 and y == 0:
        return 1
    
    if x == 0 or y == 0:
        return x + y
    
    while y > 0:
        r = x % y
        x = y
        y = r

    return x

def solve(a, b):
    if b == 0 or a == 0:
        return a, b
    
    uc = ucln(a, b)
    t = a // uc
    m = b // uc

    return t, m

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        b = randrange(max(1, min_values[i]), max_values[i])

        if i > 6:
            a = randrange(min_values[i], max_values[i] // 10)

        t, m = solve(a, b)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{a}/{b}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{t}/{m}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()