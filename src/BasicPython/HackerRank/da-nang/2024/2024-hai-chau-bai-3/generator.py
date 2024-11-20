###################################################
# Hai Chau - Da Nang - 2024 - Bai 3 - Tinh tong
###################################################

import random 
import os
import shutil
import string

min_values = [1,   1,   1,     1 ,    1 ,    10,    10,    10,    10**2, 10**3,  10**3,  10**4]
max_values = [100, 500, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11, 10**12]

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
    if n < 6:
        return 0

    used = [False] * (n + 1)
    count = 0

    for a in range(1, n+1):
        if used[a] is True:
            continue

        used[a] = True

        for c in range(1, n+1):
            if used[c] is True:
                continue

            used[c] = True

            for e in range(1, n+1):
                if used[e] is True:
                    continue

                used[e] = True

                for b in range(1, n+1):
                    if used[b] is True:
                        continue

                    tong = a + b + c
                    d = tong - c - e
                    f = tong - a -e

                    if d > 0 and d <= n and f > 0 and f <= n and used[d] is False and used[f] is False:
                        count += 1
                        #print(a, b, c, d, e, f)

                    used[b] = False
                used[e] = False
            used[c] = False
        used[a] = False

    return count

def generate():
    numbers = [7, 6, 1, 8, 9, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    for i in range(len(numbers)):
        n = numbers[i]
        r = solve(n)

        print(n, r)

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

print(solve(6))