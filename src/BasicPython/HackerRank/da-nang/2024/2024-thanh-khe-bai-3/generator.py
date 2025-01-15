##############  #####################################
# Thanh Khe - Da Nang - 2024 - Bai 3 - Xep Chu Cai
###################################################

from random import *
import os
import shutil
import string

min_values = [1,  5,  10, 20, 30, 40, 50, 60,   1, 20, 40, 50 ]
max_values = [10, 20, 50, 60, 70, 80, 90, 100, 60, 80, 90, 100]

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

def solve(n, a, m , b, k):
    if a == 'B' and b == 'B':
        return 0
    
    if n < 1 or n > 100 or m < 1 or m > 100 or k < 1 or k > m + n:
        return 0
    
    if a == 'A':
        if b == 'A':
            return min(k, n + m)
        else:
            return min(k, n)
    elif k <= n:
        return 0
    else:
        return k - n

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase, k=n))

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        a = 'A' if random() < 0.5 else 'B'
        m = randrange(min_values[i], max_values[i])
        b = 'A' if random() < 0.5 else 'B'
        k = randrange(1, m + n + 10)
        r = solve(n, a, m, b, k)

        print(f'{n} {a} {m} {b} {k} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(n), '\n', a, '\n', str(m), '\n', b, '\n', str(k), '\n'])
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

print(solve(5, 'A', 6, 'B', 7))
print(solve(5, 'B', 6, 'A', 7))
