###################################################
# Son Tra - Da Nang - 2024 - Bai 3 - Que Diem
# 2024-son-tra-bai-3-que-diem
# 2 1
# 3 7
# 4 4
# 5 2
# 6 6
# 7 8
# 8 10
# 9 18
# 10 22
# 11 20
# 12 28
# 13 68
# 14 88
# 15 108
# 16 188
# 17 200
# 18 208
# 19 288
# 20 688
# 21 888
# 22 1088
# 23 1888
# 24 2008
# 25 2088
# 26 2888
# 27 6888
# 28 8888
# 29 10888
# 30 18888
# 31 20088
# 32 20888
# 33 28888
# 34 68888
# 35 88888
# 36 108888
# 37 188888
# 38 200888
# 39 208888
# 40 288888
# 41 688888
# 42 888888
# 43 1088888
# 44 1888888
# 45 2008888
# 46 2088888
# 47 2888888
# 48 6888888
# 49 8888888
# 50 10888888
# 51 18888888
# 52 20088888
# 53 20888888
# 54 28888888
# 55 68888888
# 56 88888888
# 57 108888888
# 58 188888888
# 59 200888888
# 60 208888888
# 61 288888888
# 62 688888888
# 63 888888888
# 64 1088888888
# 65 1888888888
# 66 2008888888
# 67 2088888888
# 68 2888888888
# 69 6888888888
# 70 8888888888
# 71 10888888888
# 72 18888888888
# 73 20088888888
# 74 20888888888
# 75 28888888888
# 76 68888888888
# 77 88888888888
# 78 108888888888
# 79 188888888888
# 80 200888888888
# 81 208888888888
# 82 288888888888
# 83 688888888888
# 84 888888888888
# 85 1088888888888
# 86 1888888888888
# 87 2008888888888
# 88 2088888888888
# 89 2888888888888
# 90 6888888888888
# 91 8888888888888
# 92 10888888888888
# 93 18888888888888
# 94 20088888888888
# 95 20888888888888
# 96 28888888888888
# 97 68888888888888
# 98 88888888888888
# 99 108888888888888
###################################################

from random import *
import os
import shutil
import string

min_values = [2, 2,   2,  2,   50,  100,  1000, 5000,  10000, 25000, 50000, 75000]
max_values = [10, 20, 50, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 10**5]

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

def find_min(n):
    numbers = ['0', '0', '1', '7', '4', '2', '6', '8', '10', '18', '22', '20', '28', '68']

    if n <= 7:
        return numbers[n]

    count = n // 7
    du = n % 7

    if du == 3 and n > 10:
        return '200' + ''.join(['8'] * (count - 2))
    elif count > 1:
        return numbers[du + 7] + ''.join(['8'] * (count - 1))
    else:
        return numbers[du + 7]

def find_max(n):
    count = n // 2

    if n % 2 == 0:
        return ''.join(['1'] * count)
    else:
        return '7' + ''.join(['1'] * (count - 1))

def solve(n):
    return find_min(n), find_max(n)

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase + string.digits, k=n))

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        mi, ma = solve(n)

        #print(f'{n} {mi} {ma}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{mi}\n{ma}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

for i in range(2, 100):
    print(i, solve(i))