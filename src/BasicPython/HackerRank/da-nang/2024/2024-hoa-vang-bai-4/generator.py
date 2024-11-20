###################################################
# Hoa Vang - Da Nang - 2024 - Bai 4 - Cay Xanh
###################################################

from random import randrange
from random import choices
import os
import shutil
import string

min_values = [1, 1,   1,     10**2, 10**3, 10**4, 10**5, 10**7, 10**9,  10**10, 10**13, 10**16]
max_values = [10, 20, 10**2, 10**3, 10**4, 10**5, 10**7, 10**9, 10**10, 10**13, 10**16, 10**18]

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

def solve(a, m, l, r):
    d = (l - a) % m
    if d > 0:
        l = l - d + m

    r = r - (r - a) % m

    if r < l:
        return 0

    return (r - l) // m + 1

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase + string.digits, k=n))

def generate():
    for i in range(len(min_values)):
        a = randrange(0, max_values[i] // 3)
        m = randrange(min_values[i] // 3 + 1, max_values[i] // 3)
        l = randrange(min_values[i], max_values[i] // 2)
        r = randrange(max_values[i] // 2, max_values[i])
        s = solve(a, m, l, r)

        print(f'{a} {m} {l} {r} {s}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{a}\n{m}\n{l}\n{r}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(str(s))
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

print(solve(5, 3, 6, 15))
print(solve(1, 4, 2, 3))