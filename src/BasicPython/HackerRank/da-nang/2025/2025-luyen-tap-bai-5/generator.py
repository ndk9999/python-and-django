###################################################
# Luyen tap - 2025 - Bai 5 - Day So S
# Một số số đầu của dãy S như sau: 
# 1,4,2,3,5,7,12,10,8,6,9,11,13,15,17,24,22,20,18,16,14,19,...
# Cho số N. Hãy tính tổng các số trong dãy S từ số 
# đầu tiên cho đến số N (bao gồm cả N).
###################################################

from random import randrange
import os
import shutil
import math

KQ_MAX = 10007

min_values = [1, 1,   10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**7, 10**9,  10**11, 10**13]
max_values = [10, 20, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**9, 10**11, 10**13, 10**15]

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

def find_odd_group(n):
    g = 1

    while g * g * 2 - 1 < n:
        g += 1

    end = g * g * 2 - 1
    start = end - (g * 2 - 2) * 2

    return g * 2 - 1, start, end

def find_even_group(n):
    g = 1

    while g * (g + 1) * 2 < n:
        g += 1

    end = g * (g + 1) * 2
    start = end - (2 * g - 1) * 2
    
    return g * 2, start, end

def solve(n):
    if n % 2 == 0:
        gc, sc, ec = find_even_group(n)

        gl = gc // 2
        vtl = gl * gl
        tl = ((vtl % KQ_MAX) * (vtl % KQ_MAX)) % KQ_MAX

        vtc = ec // 2
        tc = ((vtc % KQ_MAX) * ((vtc + 1) % KQ_MAX)) % KQ_MAX

        if n > sc:
            k = (n - sc) // 2
            du = (n - 2 + sc) * k // 2
            du = du % KQ_MAX
            tc = (tc - du + KQ_MAX) % KQ_MAX
    else:
        gl, sl, el = find_odd_group(n)

        vtl = (n + 1) // 2
        tl = ((vtl % KQ_MAX) * (vtl % KQ_MAX)) % KQ_MAX
        
        gc = (gl - 1) // 2
        vtc = gc * (gc + 1)
        tc = ((vtc % KQ_MAX) * ((vtc + 1) % KQ_MAX)) % KQ_MAX

    return (tl + tc) % KQ_MAX

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        r = solve(n)

        print(f'{n} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

def generate2():
    test_cases = [2, 5, 1, 89, 499, 3870, 53143, 9270776, 40444430, 74699395177, 8328743097770, 271540735160592]

    i = 0

    for n in test_cases:
        r = solve(n)

        print(f'{n} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau5.inp'), mode='w')
        fi.write(f'{n}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau5.out'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

        i += 1

    shutil.make_archive(
        os.path.join(test_case_path, problem_name + '_test_cases'), 
        'zip', 
        os.path.join(working_dir, 'samples'))

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
# generate()
generate2()
# zip_files()

# for i in range(1, 51):
#     if i & 1 == 1:
#         print(i, find_odd_group(i))
#     else:
#         print(i, find_even_group(i))

# print(find_even_group(10**14))

# for i in range(1, 101):
#     print(f'{i} {solve(i)}')

print(solve(10**15))
print(solve(176))

# ds = []
# le = 1
# chan = 2
# for i in range(1, 101):
#     if i % 2 == 1:
#         xl = []
#         for _ in range(i):
#             xl.append(le)
#             le += 2
#         ds += xl
#     else:
#         xc = []
#         for _ in range(i):
#             xc.append(chan)
#             chan += 2
#         ds += xc[::-1]

# t = 0
# for i in range(0, len(ds)):
#     t += ds[i]
#     print(f'{ds[i]} {t}')
#     if i > 500:
#         break