#########################################################
# Tinh An Giang - 2022 - Bai 2 - Xep hinh tu que go
#########################################################

from random import randrange
import os
import shutil

min_values = [0, 0,  0,  0,     10**2, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**7]
max_values = [10, 20, 10, 10**2, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**10]

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

def solve(m, n, k):
    if (m + k * 3) % 2 == 1:
        return 'NO'
    
    if k == 1 and m + n + k < 5:
        return 'NO'
    
    if k == 0 and m + n + k < 4:
        return 'NO'
    
    return 'YES'

def generate():
    for i in range(len(min_values)):
        m = randrange(min_values[i], max_values[i])
        n = randrange(min_values[i], max_values[i])
        k = randrange(min_values[i], max_values[i])
        
        r = solve(m, n, k)
        print(f'{m} {n} {k} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{m} {n} {k}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(r)
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()