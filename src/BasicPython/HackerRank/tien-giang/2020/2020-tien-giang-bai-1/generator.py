#########################################################
# Tinh Tien Giang - 2020 - Bai 1 - Tinh dien tich HCN
#########################################################

from random import randrange
import os
import shutil

min_values = [1, 5, 10, 100, 1000, 10000, 100000, 10, 100, 1000, 10000, 100000]
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

def solve(dai, rong):
    return dai * rong

def generate():
    for i in range(len(min_values)):
        r = randrange(min_values[i], max_values[i])
        d = randrange(min_values[i], max_values[i])
        dt = solve(d, r)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(d), '\n', str(r)])
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.writelines(['Tính diện tích hình chữ nhật', '\n', str(dt)])
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()