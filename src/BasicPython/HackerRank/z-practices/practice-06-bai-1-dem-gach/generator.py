#########################################################
# Luyen tap 06 - Bai 1 - Dem so gach can lat can phong
#########################################################

import random
import math
import os
import shutil

min_values = [1,  20,  10,  100,   10**3, 10**4, 10**5, 10**6, 10,    10**2, 10**4]
max_values = [20, 100, 100, 10**3, 10**4, 10**5, 10**6, 10**7, 10**3, 10**5, 10**7]

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

def solve(d, r, n, m):
    t7 = 10**7
    t9 = 10**9

    if d <= 0 or d > t7 or r <= 0 or r > t7 or m <= 0 or m > t9 or n <= 0 or n > 100:
        return -1, -1

    total = d * r * n

    if m > total or (m + total) % 2 == 1:
        return -1, -1

    yellow = (total + m) // 2
    red = yellow - m

    return yellow, red

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        d = random.randrange(min_values[i], max_values[i])
        r = random.randrange(min_values[i], max_values[i])
        n = random.randrange(1, 101)

        s = d * r * n

        if s < 10**9:
            m = random.randrange(1, s)
        else:
            m = random.randrange(1, 10**9)

        if (s + m) % 2 == 1:
            m += 1

        yellow, red = solve(d, r, n, m)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{d}\n{r}\n{n}\n{m}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{yellow}\n{red}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

# create_folders()
# generate()
zip_files()

print(solve(8, 6, 12, 120))
print(solve(9111799, 3350208, 21, 941994921))