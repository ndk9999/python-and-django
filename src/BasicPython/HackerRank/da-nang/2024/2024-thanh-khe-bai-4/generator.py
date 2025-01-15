###################################################
# Thanh Khe - Da Nang - 2024 - Bai 4 - Doi qua
###################################################

from random import *
import os
import shutil
import string

min_values = [2,  2,  2,     10**2, 10**3, 10**4, 10**5, 10**6, 10**8,  10**10, 10**12, 10**15]
max_values = [30, 50, 10**2, 10**3, 10**4, 10**5, 10**6, 10**8, 10**10, 10**12, 10**15, 10**18]

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

def solve(n, a, b, c):
    # Tinh gia mua chai thuy tinh sau khi tra lai chai
    d = b - c

    # Neu gia hop <= gia chai, uu tien mua sua hop
    if a <= d:
        return n // a
    
    # Nguoc lai, neu gia hop > gia chai thi uu tien mua sua chai
    lit = (n - b) // d
    du = n - lit * d

    if du >= b:
        lit += 1
        du = du - b + c

    lit += du // a
    du = du % a

    return lit

def rand_string(n):
    return ''.join(choices(string.ascii_lowercase + string.digits, k=n))

def generate():
    for i in range(len(min_values)):
        n = randrange(max_values[i] // 2, max_values[i])
        a = randrange(1, max_values[i] // 2)
        b = randrange(10, max_values[i] // 2)

        if i <= 8:
            a = randrange(1, min(max_values[i] // 2, 10**5))
            b = randrange(10, min(max_values[i] // 2, 10**5))

        c = randrange(1, b)
        r = solve(n, a, b, c)

        #print(f'{n} {mi} {ma}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}\n{a}\n{b}\n{c}')
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

print(10, 4, 9, 8, solve(10, 4, 9, 8))
print(10, 5, 6, 1, solve(10, 5, 6, 1))
print(30, 5, 16, 12, solve(30, 5, 16, 12))