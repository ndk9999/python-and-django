###################################################
# Hai Chau - Da Nang - 2024 - Bai 2 - Dem So
###################################################

from random import randrange
from random import choices
import os
import shutil
import string

min_values = [1,   1,   1,     1 ,    1 ,    10,    10,    10,    10**2, 10**3,  10**3,  10**4]
max_values = [100, 500, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11, 10**12]

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

def build_a():
    a = [1, 2]
    t = 1
    g = 2
    s = t * g

    while s < 10**12:
        a.append(s)
        t = g
        g = s
        s = t * g

    return a

def solve(numbers):
    numbers = list(numbers)
    kq = []

    for x in numbers:
        if a.count(x) > 0:
            kq.append(x)

    return sorted(kq)

def generate():
    for i in range(len(min_values)):
        m = randrange(0, len(a))
        n = randrange(1, 100 - m)

        numbers = [randrange(min_values[i] + vt % 10, max_values[i]) for vt in range(n)]

        for vt in range(m):
            numbers.insert(randrange(0, len(numbers)), a[randrange(0, len(a))])
        
        r = solve(numbers)

        print(m, r)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(';'.join(str(k) for k in numbers))
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{len(r)}\n')

        for k in r:
            fo.write(f'{k}\n')

        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

a = build_a()
create_folders()
generate()
zip_files()

print(solve([8, 256, 45]))