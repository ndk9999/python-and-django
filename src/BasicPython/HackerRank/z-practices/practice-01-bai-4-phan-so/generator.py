#########################################################
# Luyen tap 01 - Bai 4 - Tinh tong va toi gian phan so
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  1,  0,  0,  0,     10,    100,   10**2, 10**3, 10**4, 10**6, 10**7]
max_values = [10, 20, 10, 10, 10**2, 10**2, 10**3, 10**6, 10**6, 10**6, 10**9, 10**9]

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

def solve(a, b, c, d):
    t = 0
    m = 0
    
    if b == 0 or d == 0:
        return t, m
    
    if a == 0:
        t = c
        m = d
    elif c == 0:
        t = a
        m = b
    else:
        t = a * d + b * c
        m = b * d

    uc = ucln(t, m)
    t = t // uc
    m = m // uc

    return t, m

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        b = randrange(min_values[i], max_values[i])
        c = randrange(min_values[i], max_values[i])
        d = randrange(min_values[i], max_values[i])
        t, m = solve(a, b, c, d)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(a), '\n', str(b), '\n', str(c), '\n', str(d)])
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')

        if t == 0 and m == 0:
            fo.write('ERROR')
        else:
            fo.write(f'{t}/{m}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()