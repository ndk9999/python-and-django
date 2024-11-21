###################################################
# Son Tra - Da Nang - 2024 - Bai 4 - Duong Day Dien
###################################################

from random import *
import os
import shutil
import string

min_values = [1,  1,  1,     10,    10**2, 10**3, 10**4, 10**5, 10**8,  10**10, 10**12, 10**15]
max_values = [15, 30, 10**2, 10**3, 10**4, 10**5, 10**7, 10**9, 10**11, 10**13, 10**15, 10**18]

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

def solve(left, right):
    n = 0
    temp = right

    while temp > 0:
        n += 1
        temp = temp >> 1

    t = 0

    for i in range(1, n+1):
        s = 1 << i
        d = 1 << (i + 1)

        cl = 0
        cr = 0

        if s < left:
            cl = (left - 1 - s) // d + 1

        if s < right:
            cr = (right - s) // d + 1

        t += i * (cr - cl)

    return t

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase + string.digits, k=n))

def generate():
    for i in range(len(min_values)):
        right = randrange(min_values[i], max_values[i])
        left = randrange(1, right + 1)
        r = solve(left, right)

        #print(f'{n} {mi} {ma}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{left} {right}')
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

print(2, 10, solve(2, 10))
print(13, 17, solve(13, 17))
print(13, 157, solve(13, 157))