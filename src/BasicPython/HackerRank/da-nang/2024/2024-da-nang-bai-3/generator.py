###################################################
# Thanh Pho Da Nang - 2024 - Bai 3 - Vi Tri Xau Con
###################################################

from random import randrange
from random import choices
import os
import shutil
import string

min_values = [1, 1,   1,  10,    10,    10**2, 10**3, 1,  10,    10,    10**2, 10**3]
max_values = [10, 20, 10, 10**2, 10**3, 10**4, 10**4, 10, 10**2, 10**3, 10**4, 10**4]

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

def solve(s, t):
    return t.rfind(s) + 1

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase + string.digits, k=n))

def generate():
    for i in range(len(min_values)):
        ls = randrange(1, min(100, max_values[i]))
        lt = randrange(min_values[i], max_values[i])
        s = rand_string(ls)
        t = rand_string(lt)
        k = randrange(1, lt)
        t = t[:k] + s + t[k:]
        r = solve(s, t)

        print(f'{s} {t} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([s, '\n', t])
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(str(r))
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

# 108452 YES
# 212523 YES
# 52576148 YES
# 502705804830 YES
# 5642003329652 YES
# 17862943368599124 YES

