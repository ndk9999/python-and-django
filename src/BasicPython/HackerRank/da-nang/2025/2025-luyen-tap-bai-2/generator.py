###################################################
# Luyen tap - 2025 - Bai 2 - Xep Bi
# Hải rất thích các viên bi nhiều màu sặc sỡ. Để 
# thưởng cho thành tích học tập tốt của Hải, bố 
# của Hải đã mua cho bạn rất nhiều bi. Hải cho 
# các viên bi vào hộp lần lượt theo thứ tự là: 
# Xanh - Đỏ - Vàng - Đỏ - Trắng rồi lại đến bi 
# Xanh - Đỏ - Vàng - Đỏ - Trắng ... cứ như vậy. 
# Hỏi muốn trong hộp có N viên bi đỏ thì phải bỏ 
# vào đó ít nhất bao nhiêu viên bi?
###################################################

from random import randrange
import os
import shutil
import math

min_values = [1, 1,   10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**8,  10**10, 10**4]
max_values = [10, 20, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**8, 10**10, 10**12, 10**7]

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
    luot = n // 2
    
    if n % 2 == 0:
        return luot * 5 - 1
    else:
        return luot * 5 + 2

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
    test_cases = [2, 6, 1, 93, 908, 3642, 80169, 804060, 22594319, 7887792082, 987885951573, 7410404]

    i = 0

    for n in test_cases:
        r = solve(n)

        print(f'{n} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau2.inp'), mode='w')
        fi.write(f'{n}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau2.out'), mode='w', encoding='utf-8')
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
#generate()
generate2()
zip_files()

print(solve(1))
print(solve(2))
print(solve(3))
print(solve(4))
print(solve(20))
