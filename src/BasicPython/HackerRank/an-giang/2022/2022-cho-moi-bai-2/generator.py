###################################################
# Cho Moi - An Giang - 2022 - Bai 2 - So May Man
###################################################

from random import randrange
import os
import shutil

min_values = [10**4, 10**5, 0,     0,     10**4, 10**6, 10**7, 10**9,  10**9,  10**11, 10**14, 10**14]
max_values = [10**5, 10**6, 10**5, 10**6, 10**7, 10**8, 10**9, 10**12, 10**13, 10**14, 10**17, 10**17]

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

def solve(n):
    if n < 1000 or n > 10 ** 17:
        return 'NO'

    digits = [int(c) for c in str(n)]
    chan = sum([x for idx, x in enumerate(digits) if idx % 2 == 1 and x % 2 == 0])
    le = sum([x for idx, x in enumerate(digits) if idx % 2 == 0 and x % 2 == 1])

    # chan = 0
    # le = 0
    
    # for i in range(0, len(digits)):
    #     if i % 2 == 1 and digits[i] % 2 == 0:
    #         chan += digits[i]
    #     if i % 2 == 0 and digits[i] % 2 == 1:
    #         le += digits[i]

    return 'YES' if chan > 0 and chan == le else 'NO'

def generate():
    numbers = [
        1232,
        219056,
        78309,
        108452,
        1657479,
        52576148,
        926404675,
        502705804830,
        8255593931900,
        5642003329652,
        17862943368599124,
        14264355286310631,
    ]

    for i in range(len(numbers)):
        n = numbers[i]
    # for i in range(len(min_values)):
    #     n = randrange(min_values[i], max_values[i])
        r = solve(n)

        print(f'{n} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(str(n))
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

# 108452 YES
# 212523 YES
# 52576148 YES
# 502705804830 YES
# 5642003329652 YES
# 17862943368599124 YES

