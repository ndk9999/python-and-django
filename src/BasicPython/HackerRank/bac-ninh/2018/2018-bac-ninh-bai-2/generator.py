#########################################################
# Tinh Bac Ninh - 2018 - Bai 2 - Tim tat ca uoc chung
#########################################################

from random import randrange
import os
import shutil

min_values = [4,  20, -10, -100, 100,   100,  1000,  10000,  100000,  100000,  1000000,  1000000]
max_values = [20, 50, 100, 1000, 10000, 1000, 10000, 100000, 1000000, 1000000, 10000000, 10000000]

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

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def solve(a, b):
    if a <= 0 or b <= 0:
        return 0
    
    max_cd = gcd(a, b)
    sum = 0

    for i in range(1, max_cd + 1):
        if max_cd % i == 0:
            sum += i

    return sum

def generate():
    for i in range(len(min_values)):
        a = randrange(min_values[i], max_values[i])
        b = randrange(min_values[i], max_values[i])

        r = solve(a, b)
        print(a, b, r)
        
        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.writelines([str(a), '\n', str(b)])
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

#print(solve(943629, 943629))