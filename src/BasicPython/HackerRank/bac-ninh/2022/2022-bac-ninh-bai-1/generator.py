#########################################################
# Thuan Thanh - Bac Ninh - 2022 - Bai 1 - Xuat hien nhieu nhat
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

def solve(file):
    fi = open(file, mode='r', encoding='utf-8')
    n = int(fi.readline())
    list = [0] * 1001

    for _ in range(n):
        k = int(fi.readline())
        list[k] = list[k] + 1

    fi.close()

    dem = list[0]
    m = 0

    for k in range(1, 1001):
        if list[k] >= dem:
            dem = list[k]
            m = k

    return m, dem

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(n), '\n'])

        for _ in range(n):
            x = randrange(0, 1001)
            fi.writelines([str(x), '\n'])

        fi.close()

        m, c = solve(os.path.join(input_path, f'input{i:02d}.txt'))
        print(n, m, c)

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{m} {c}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()
