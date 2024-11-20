###################################################
# Thanh pho Vung Tau - 2020 - Bai 2 - Thu hoach tao
###################################################

from random import randrange
import os
import shutil

min_values = [1, 1,  -5,  -50,  -100,   10**3, 10**4, 10**6, 10**6, 10**8, 10**10, 10**13]
max_values = [10, 20, 20, 10**2, 10**3, 10**5, 10**6, 10**7, 10**8, 10**10, 10**13, 10**15]

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

def solve(n, k):
    if n < 1 or n >= 10 ** 15:
        return 0
    
    if k <= 1 or k > 100 or k % 2 == 1:
        return 0

    chia3 = n // 3
    chia5 = n // 5
    chia15 = n // 15
    thuong = n - chia3 - chia5 + chia15

    return thuong * k + chia15 * k // 2 + (chia3 + chia5 - 2 * chia15) * k * 2

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        k = randrange(-10, 110)
        r = solve(n, k)

        print(f'{n} {k} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n} {k}')
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