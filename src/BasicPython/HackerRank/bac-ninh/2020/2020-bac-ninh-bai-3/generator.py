#########################################################
# TP Bac Ninh - 2020 - Bai 3 - Chon keo
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  5,  1,   10,   100,   10000,  100000, 1,   10,   100,   10000,  100000]
max_values = [10, 20, 100, 1000, 10000, 100000, 1000000, 100, 1000, 10000, 100000, 1000000]

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

def solve(n, m, p, q):
    if p == 0 or q == 0 or m < 3 or n < 5 or n > 20:
        return 0

    dem = 0

    for x in range(p, n + 1):
        for d in range(q, n + 1):
            v = m - x - d
            if v > 0:
                dem += 1

    return dem

def generate():
    for i in range(len(min_values)):
        n = randrange(5, 20)
        m = randrange(0, 3 * n + 1)
        p = randrange(0, n + 1)
        q = randrange(0, n + 1)

        r = solve(n, m, p, q)
        print(n, m, p, q, r)
        
        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(n), '\n', str(m), '\n', str(p), '\n', str(q)])
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

#print(solve(10, 20, 3, 7))