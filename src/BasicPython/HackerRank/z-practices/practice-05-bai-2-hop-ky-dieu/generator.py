#########################################################
# Luyen tap 05 - Bai 2 - Chiec hop dieu ky
#########################################################

import random
import math
import os
import shutil

min_values = [1,  5,  5,  20,  100,   10**3, 10**4, 10,    10**2,  10**3,  10**4, 10**3]
max_values = [10, 20, 50, 100, 10**3, 10**4, 10**5, 10**2, 10**3,  10**4,  10**5, 10**5]

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

def solve(n, q, ingredients, queries):
    answers = []
    k = min(n, max(queries))
    j = 0
    yellow = 0
    orange = 0
    red = 0

    for i in range(1, k+1):
        if ingredients[i-1] == 1:
            yellow += 1
        elif ingredients[i-1] == 2:
            orange += 1
        else:
            red += 1

        if yellow == 2:
            orange += 1
            yellow = 0

        if orange == 2:
            red += 1
            orange = 0

        print(i, yellow, orange, red)

        if i == queries[j]:
            answers.append(yellow + orange + red)
            j += 1

    return answers

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        n = random.randrange(min_values[i], max_values[i])
        q = random.randrange(1, n + 1)

        ingredients = [random.randrange(0, 3) + 1 for _ in range(n)]
        times = [x for x in range(1, n+1)]
        m = len(times)

        while q < m:
            idx = random.randrange(0, m)
            del times[idx]
            m -= 1

        answers = solve(n, q, ingredients, times)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n} {q}\n')
        fi.write(' '.join([str(x) for x in ingredients]))
        fi.write('\n')
        fi.write(' '.join([str(x) for x in times]))
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(' '.join([str(x) for x in answers]))
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

# create_folders()
# generate()
# zip_files()

print(solve(10, 5, [1, 2, 3, 1, 2, 1, 3, 2, 1, 1], [3, 5, 6, 8, 10]))
print(solve(6, 6, [1, 3, 2, 2, 1, 2], [1, 2, 3, 4, 5, 6]))
print(solve(25, 1, [2, 2, 1, 3, 1, 1, 3, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 3, 2], [6]))