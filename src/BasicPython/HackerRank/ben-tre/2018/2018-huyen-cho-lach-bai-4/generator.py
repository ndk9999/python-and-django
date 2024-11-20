#########################################################
# Huyen Cho Lach - Ben Tre - 2018 - Bai 4 - Vong Tron So
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  2,  1, 10, 30, 50,  70, 100, 200, 300, 500, 750]
max_values = [6, 10, 10, 30, 50, 70, 100, 200, 300, 500, 750, 1000]

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
    if n < 2 or n > 1000 or k < 1 or k > n // 2:
        return 0
    
    canh = n
    dau = 1

    for i in range(k - 1):
        dau += (canh - 1) * 4
        canh -= 2
        
    cuoi = dau + (canh - 1) * 4 - 1

    return (dau + cuoi) * (cuoi - dau + 1) // 2

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        k = randrange(0, n // 2 + 2)
        s = solve(n, k)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n} {k}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{s}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

#print(solve(6,3))