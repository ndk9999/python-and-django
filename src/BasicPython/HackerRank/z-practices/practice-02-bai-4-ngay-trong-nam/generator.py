#########################################################
# Luyen tap 01 - Bai 1 - Boc bi
#########################################################

from random import randrange
import os
import shutil

so_ngay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 32]
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

def solve(d, m, y):
    if m < 1 or m > 12:
        return 0
    
    if y < 1 or y > 9999:
        return 0
    
    ntd = so_ngay[m]

    if is_leap_year(y) and m == 2:
        ntd = 29

    if d < 1 or d > ntd:
        return 0
    
    days = 0
    for i in range(m):
        days += so_ngay[i]

    return days + d

def generate():
    for i in range(len(min_values)):
        y = randrange(min_values[i], max_values[i])
        m = randrange(0, 13)
        if m == 2:
            d = randrange(28, 32)
        else:
            d = randrange(0, 35)
        r = solve(d, m, y)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{d}\n{m}\n{y}')
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

print(1, 1, 2025, solve(1, 1, 2025))
print(10, 1, 2025, solve(10, 1, 2025))
print(11, 2, 2025, solve(11, 2, 2025))
print(1, 3, 2025, solve(1, 3, 2025))
print(25, 11, 2025, solve(25, 11, 2025))