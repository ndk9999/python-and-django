###################################################
# Quan Son Tra - 2025 - Bai 3 - Hai Tao
###################################################

from random import randrange
import os
import shutil
import math

min_values = [1, 1,   10**0, 10**2, 10**3, 10**4, 10**5, 10**6, 10**8,  10**10, 10**12, 10**14]
max_values = [10, 20, 10**2, 10**3, 10**4, 10**5, 10**6, 10**8, 10**10, 10**12, 10**14, 10**15]

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

def sum_digits(n):
    s = 0

    while n > 0:
        s += n % 10
        n //= 10

    return s

def is_round_number(n):
    return (n + sum_digits(n)) % 10 == 0

def solution1(n):
    # In the sequence of numbers 0, 5, 24, 29, 43, 48, 62, 67, 81, 86, ..., 
    # two numbers combine into a pair and they differ by 5 units.
    # For each number, we split it into 2 parts: left and right.
    # The right part contains only the units digit. 
    # The left part contains the remaining digits.
    # We first determine the left part and then append a digit to find the round number

    # So, in the first step, we determine the position of the pair
    # For example, with n = 7, pos = (7 + 1) // 2 = 4 (fourth pair)
    pos = (n + 1) // 2

    # Then we compute the left part
    # For example, with n = 7, pos = 4, we need to find the left part of 6
    left = pos * 2 - 2

    # The sum of digits in the left part must be an even number
    # For example, with n = 14, the round number is 138
    # In this case, pos = 7, left = 12 so we need to increase it 1
    left += sum_digits(left) % 2

    # Try to find the first number of the pair at position pos
    # by adding 1 more digit to the left part and check if it
    # results in a round number
    k = left * 10

    while not is_round_number(k):
        k += 1

    # If the input position is even, it means we need to find the
    # second number in the pair and it should be first number + 5
    if n % 2 == 0:
        k += 5

    return k

def solution2(n):
    # In this solution, we have a comment:
    # The round numbers from position 11 onwards are all 9 or 10 times larger than their positions.
    # If the round number is 10 times larger than its position, the remainder of dividing the round 
    # number by its position is very small. Therefore, we will move forward to find the round number.
    # If the round number is 9 times larger than its position, the remainder of dividing the round number 
    # by its position is very large, almost equal to its position. Therefore, we will move backward to find the round number.
    # Only round numbers in odd positions and the sum of the digits is even will have a round number 10 times larger than its position.
    # The first 10 round numbers do not follow this rule, so we will calculate in a different way. 

    numbers = [0, 0, 5, 24, 29, 43, 48, 62, 67, 81, 86]

    # Handle the special cases
    if n < 11:
        return numbers[n]
    
    # Handle the round number that follow the pattern
    d = -1
    k = n * 10
    odd = False

    # Case 1: round number is 10 times larger than its position
    # We start from n * 10, increase 1-by-1 to find the result
    if n % 2 == 1 and sum_digits(n // 10) % 2 == 1:
        d = 1
    # Case 2: the round number is at odd position, we will find
    # the next round number and then subtract it by 5
    elif n % 2 == 1:
        k += 9
        odd = True
    # Case 3: the round number is at even position, we start from
    # n * 10 - 1 and decrease 1-by-1 to find the result
    else:
        k -= 1

    # Try to find the round number
    while not is_round_number(k):
        k += d

    # If the input position is odd, it means we need to find the
    # first round number of the pair. It should be k - 5.
    if odd:
        k -= 5

    return k


def solve(n):
    return solution1(n)
    # return solution2(n)

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
    test_cases = [3, 9, 21, 501, 8688, 65435, 445318, 62092771, 3184838108, 962402876531, 70010631296025, 814652557954390]

    i = 0

    for n in test_cases:
        r = solve(n)

        print(f'{n} {r}')

        sample_path = os.path.join(working_dir, 'samples', f'test-case-{i}')

        if not os.path.exists(sample_path):
            os.makedirs(sample_path)

        fi = open(os.path.join(sample_path, f'cau1.inp'), mode='w')
        fi.write(f'{n}')
        fi.close()

        fo = open(os.path.join(sample_path, f'cau1.out'), mode='w', encoding='utf-8')
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
generate()
generate2()
zip_files()

print(solve(17))
print(solve(145))
print(solve(146))
print(solve(307))
print(solve(308))

# for i in range(10 ** 14, 10 ** 14 + 1000):
#     s1 = solution1(i)
#     s2 = solution2(i)

#     if (s1 == s2):
#         print(f'{i}\t{s1}\t{s2}')
#     else:
#         print(f'{i}\t{s1}\t{s2} <==================')