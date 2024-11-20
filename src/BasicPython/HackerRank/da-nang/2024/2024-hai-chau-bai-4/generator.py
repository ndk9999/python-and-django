###################################################
# Hai Chau - Da Nang - 2024 - Bai 4 - So nho nhat
###################################################

from random import randrange
from random import choices
import os
import shutil
import string

min_values = [1, 1,  1, 1 , 5 , 10, 15, 20, 30, 40, 50, 80]
max_values = [5, 10, 5, 10, 15, 20, 20, 30, 40, 50, 80, 100]

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

def solve(n, s):
    if s > n * 9:
        return 'NO'
    
    if s == 0 and n > 1:
        return 'NO'
    
    if n == 1 and s < 10:
        return str(s)
    
    digits = [0] * n
    vt = n - 1

    while vt >= 0 and s > 0:
        if s < 9:
            digits[vt] = s
            s = 0
        else:
            digits[vt] = 9
            s -= 9
        vt -= 1

    if vt >= 0:
        digits[0] = 1
        digits[vt + 1] -= 1

    return ''.join(str(x) for x in digits)

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        s = randrange(0, n * 9 * 3 // 2)
        r = solve(n, s)

        print(n, s, r)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}\n{s}')
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

print(solve(3, 17))
print(solve(5, 50))