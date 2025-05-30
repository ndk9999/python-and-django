#########################################################
# Tinh Lam Dong - 2024 - Bai 4 - Cap so dac biet
#########################################################

from random import *
import os
import shutil
import string

min_values = [1,  10,  1,     10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10]
max_values = [10, 100, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**12]

working_dir = os.path.dirname(os.path.realpath(__file__))
problem_name = os.path.split(working_dir)[-1]
zip_file_path = os.path.join(working_dir, 'zipped-files')
test_case_path = os.path.join(working_dir, 'test-cases')
input_path = os.path.join(test_case_path, 'input')
output_path = os.path.join(test_case_path, 'output')

def create_folders():
    if not os.path.exists(zip_file_path):
        os.makedirs(zip_file_path)

    if not os.path.exists(test_case_path):
        os.makedirs(test_case_path)

    if not os.path.exists(input_path):
        os.makedirs(input_path)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

def rand_string(n):
    return ''.join(choices(string.ascii_uppercase, k=n))

def solve(s, n, c):
    m = len(s)
    dc = s.count(c)

    if dc == 0 or m == 0:
        return 0
    
    loop = n // m
    rem = n % m
    kq = loop * dc

    if rem > 0:
        k = loop % m
        t = s

        if k > 0:
            t = s[m-k:] + s[0:m-k]

        kq += t[0:rem+1].count(c)

    return kq

def generate():
    for i in range(len(min_values)):
        k = randrange(1, 100)
        s = rand_string(k)
        n = randrange(min_values[i], max_values[i])
        c = string.ascii_uppercase[randrange(0, 26)]
        r = solve(s, n, c)

        print(s, n, c, r)

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{s}\n{n}\n{c}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(str(r))
        fo.close()

def generate2():
    for i in range(100):
        p = i % 10 + 2
        k = randrange(1, 100)
        s = rand_string(k)
        n = randrange(min_values[p], max_values[p])
        c = string.ascii_uppercase[randrange(0, 26)]
        r = solve(s, n, c)
        print(f'{s} {n} {c} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau4.inp'), mode='w')
        fi.write(f'{s}\n{n}\n{c}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau4.out'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

        i += 1

    shutil.make_archive(
        os.path.join(zip_file_path, problem_name + '_test_cases'), 
        'zip', 
        os.path.join(working_dir, 'samples'))

def zip_files():
    shutil.make_archive(os.path.join(zip_file_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
generate2()
zip_files()

print(solve('asdf', 7, 's'))
print(solve('asdf', 7, 'k'))
print(solve('fadfdrfqwer', 4, 'f'))