#########################################################
# Luyen tap 04 - Bai 4 - Tro choi lat dong xu
#########################################################

import random
import math
import os
import shutil

min_values = [2,  2,  2,   100,   10**3,  10**4,  10**5, 10**6, 10**7,  10**8,  10**2,  10**6]
max_values = [10, 50, 100, 10**3, 10**4,  10**5,  10**6, 10**7, 10**8,  10**9,  10**5,  10**9]

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

def count_divisors(n, m):
    k = min(m, int(math.sqrt(n)))
    c = 0

    for i in range(1, k+1):
        if n % i > 0:
            continue

        if i <= m:
            c += 1

        if n // i <= m and i * i < n:
            c += 1

    return c

def count_multipliers(s, n):
    return (n - s) // s + 1

def solve(n, m, w):
    first = 0
    second = 0

    # Calculate the total number of coins flipped by each player
    for i in range(1, m+1):
        k = count_multipliers(i, n)
        print(i, k)

        if i % 2 == 1:
            first += k
        else:
            second += k

    # Determine the status of the last coin
    dc = count_divisors(n, m)
    hs = 'H' if dc % 2 == 0 else 'S'

    if first % 2 == second % 2:
        return 'H', hs
    elif first % 2 == 0:
        return w, hs
    elif w == 'A':
        return 'B', hs
    else:
        return 'A', hs

def generate():
    for i in range(len(min_values)):
        print(f'Generating test case {i}')

        n = random.randrange(min_values[i], max_values[i])
        m = random.randrange(2, min(10**5, n))
        w = 'A' if random.randrange(0, 10) < 5 else 'B'

        a, c = solve(n, m, w)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n} {m} {w}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.writelines([a, '\n', c])
        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

# create_folders()
# generate()
# zip_files()

print(solve(10, 8, 'A'))
print(solve(10, 8, 'B'))