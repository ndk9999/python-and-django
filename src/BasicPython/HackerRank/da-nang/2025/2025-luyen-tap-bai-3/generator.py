###################################################
# Luyen tap - 2025 - Bai 3 - Mua Vo
# Vào dịp tổng kết năm học sắp tới, nhà trường cần 
# N quyển vở để trao thưởng cho các học sinh có 
# thành tích học tập tốt. Mỗi quyển vở có giá 8 
# nghìn đồng. Nhà sách ABC đang có chương trình 
# khuyến mãi: cứ mua X quyển sẽ được tặng thêm Y 
# quyển. Hãy tính số tiền ít nhất phải trả để mua 
# số vở đủ để trao thưởng.
###################################################

from random import randrange
import os
import shutil
import math

min_values = [1, 1,   10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**3]
max_values = [10, 20, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**6]

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

def solve(n, x, y):
    xy = x + y
    luot = n // xy
    du = n % xy
    
    return (luot * x + du) * 8

def generate():
    for i in range(len(min_values)):
        n = randrange(min_values[i], max_values[i])
        x = randrange(1, 1001)
        y = randrange(1, x + 1)
        r = solve(n, x, y)

        print(f'{n} {x} {y} {r}')

        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{n}\n{x}\n{y}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        fo.write(f'{r}')
        fo.close()

def generate2():
    test_cases = [
        [5, 2, 2],
        [7, 10, 3],
        [11, 5, 1],
        [69, 15, 4],
        [486, 26, 5],
        [6043, 936, 73],
        [95108, 555, 60],
        [528402, 824, 113],
        [4323751, 822, 468],
        [24925857, 892, 371],
        [794882386, 601, 474],
        [466539, 36, 23],
    ]

    i = 0

    for [n, x, y] in test_cases:
        r = solve(n, x, y)

        print(f'{n} {x} {y} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau3.inp'), mode='w')
        fi.write(f'{n}\n{x}\n{y}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau3.out'), mode='w', encoding='utf-8')
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

print(solve(5, 2, 2))
print(solve(10, 3, 1))
print(solve(20, 3, 1))
print(solve(55, 4, 3))
print(solve(19, 1, 0))
