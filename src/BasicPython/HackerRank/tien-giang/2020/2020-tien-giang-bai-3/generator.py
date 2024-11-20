#########################################################
# Tinh Tien Giang - 2020 - Bai 3 - Ban vit
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  5,  1,  21, 51,  101, 202, 401, 601, 801,  1,  101]
max_values = [10, 20, 20, 50, 100, 200, 400, 600, 800, 1000, 100, 1000]

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

def solve(n, fo):
    if n < 1 or n > 1000:
        return 0
    
    dem = 0

    for loai_1 in range(n // 5 + 1):
        loai_2 = n - loai_1 * 5
        if loai_2 >= 0 and loai_2 % 2 == 0:
            dem += 1
            fo.write(f'{loai_1} {loai_2 // 2}\n')

    return dem

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        
        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(str(n))
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        
        if solve(n, fo) == 0:
            fo.write('0')

        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()