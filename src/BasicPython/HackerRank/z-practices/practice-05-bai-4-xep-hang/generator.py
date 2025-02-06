#########################################################
# Luyen tap 04 - Bai 3 - So may man va gan may man
#########################################################

import random
import math
import os
import shutil

min_values = [0,  0,  0,   100,   10**3,  10**4,  0,    100,    10**3,  10**4,  10**2,  10**3]
max_values = [10, 50, 100, 10**3, 10**4,  10**5,  100,  10**3,  10**4,  10**5,  10**4,  10**5]

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

def solve(n, scores):
    if n < 4 or n % 4 > 0:
        return -1, -1, -1

    m = n // 4
    scores = sorted(scores, reverse=True)

    if scores[m-1] == scores[m] or scores[2*m-1] == scores[2*m] or scores[3*m-1] == scores[3*m]:
        return -1, -1, -1

    return scores[m-1], scores[2*m-1], scores[3*m-1]

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        n = random.randrange(1, (max_values[i] - min_values[i]) // 4) * 4 + min_values[i]
        scores = [random.randint(0, 101) for _ in range(n)]

        a, b, c = solve(n, scores)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}\n')
        fi.write(' '.join([str(x) for x in scores]))
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        
        if a < 0:
            fo.write('-1')
        else:
            fo.write(f'{a} {b} {c}')

        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

# create_folders()
# generate()
zip_files()

print(solve(4, [90, 25, 60, 75]))
print(solve(8, [27, 29, 92, 92, 67, 67, 85, 92]))
print(solve(8, [0, 1, 2, 3, 4, 5, 6, 7]))