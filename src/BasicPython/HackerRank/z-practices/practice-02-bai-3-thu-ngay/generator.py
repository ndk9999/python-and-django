#########################################################
# Luyen tap 01 - Bai 1 - Boc bi
#########################################################

from random import randrange
import os
import shutil

thu = ['Thu Hai', 'Thu Ba', 'Thu Tu', 'Thu Nam', 'Thu Sau', 'Thu Bay', 'Chu Nhat']
min_values = [2000, 2024, 1,    1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 2000]
max_values = [2024, 2100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9999, 2100]

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

def is_leap_year(n):
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)

def solve(n):
    count = 0
    year = abs(n - 2024)

    m = n
    while m > 2024:
        if is_leap_year(m-1):
            count += 1
        m -= 1

    while m < 2024:
        if is_leap_year(m):
            count += 1
        m += 1

    days = year * 365 + count

    if n < 2024:
        return thu[(7 - days % 7) % 7]
    else:
        return thu[days % 7]

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        r = solve(n)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}')
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

# for y in range(2000, 2040):
#     print(y, solve(y))