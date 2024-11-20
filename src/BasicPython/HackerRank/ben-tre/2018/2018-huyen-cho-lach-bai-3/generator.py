#########################################################
# Huyen Cho Lach - Ben Tre - 2028 - Bai 2 - Dem ky tu
#########################################################

from random import randrange
import os
import shutil

min_values = [1,  1,   1,     10,    10**3, 10**4,  10**5,  10**6,  10**8,  10**10, 10**12, 10**14]
max_values = [50, 100, 10**2, 10**3, 10**4, 10**5,  10**6,  10**8,  10**10, 10**12, 10**14, 10**15]

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

def solve(s, n):
    d = n + 1
    if n == 0 or s < d or (s + d) % 2 == 1:
        return 0, 0
    
    x = (s - d) // 2
    y = s - x

    return x, y    

def generate():
    for i in range(len(min_values)):
        s = randrange(min_values[i], max_values[i])
        n = randrange(0, 500)

        if i > 9:
            n = randrange(50001, 5000000)
        elif i > 6:
            n = randrange(501, 50000)
        elif i < 2:
            n = randrange(0, min(s, 20))

        small, big = solve(s, n)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{s} {n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{small} {big}')
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()

a, b = solve(828, 15)
print(a, b)