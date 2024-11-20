#########################################################
# Tinh An Giang - 2022 - Bai 3 - Tim so ga moi loai
#########################################################

from random import randrange
import os
import shutil

min_values = [2, 5, 1, 3, 1, 3, 1, 2, 4, 2, 3, 4]
max_values = [5, 3, 5, 4, 2, 2, 1, 2, 5, 1, 3, 1]

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

def solve(m, n, fo):
    dem = 0
    
    for trong in range(1, 100 // m):
        tien_con = 100 - m * trong
        for mai in range(1, tien_con // n):
            ga_con = 100 - trong - mai

            if ga_con > 1 and ga_con % 2 == 0 and ga_con // 2 + trong * m + mai * n == 100:
                dem += 1
                fo.write(f'{trong} {mai} {ga_con}\n')

    return dem

def generate():
    for i in range(len(min_values)):
        #m = randrange(min_values[i], max_values[i])
        #n = randrange(min_values[i], max_values[i])
        m, n = min_values[i], max_values[i]
        
        fi = open(os.path.join(input_path, f'input{i:02d}.txt'), mode='w')
        fi.write(f'{m}\n{n}')
        fi.close()

        fo = open(os.path.join(output_path, f'output{i:02d}.txt'), mode='w', encoding='utf-8')
        
        dem = solve(m, n, fo)
        print(f'So dap an: {dem}')

        if dem == 0:
            fo.write('0 0 0')

        fo.close()

def zip_files():
    shutil.make_archive(os.path.join(test_case_path, problem_name), 'zip', test_case_path)

print(f'Generating test cases for the problem {problem_name}')

create_folders()
generate()
zip_files()