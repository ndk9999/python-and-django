def pow_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp & 1 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp >> 1
    return result

def pow_mod_recursive(base, exp, mod):
    if exp <= 0:
        return 1
    
    if exp == 1:
        return base % mod

    result = pow_mod_recursive(base, exp >> 1, mod)
    result = (result * result) % mod

    if exp & 1 == 1:
        result = (result * base) % mod

    return result


def legoBlocks(n, m):
  modulo = 10 ** 9 + 7
  # calculate num_permutations for one line
	# base cases:
	# (1, 1): (1,)
	# (1, 2): ((1, 1), (2,))
	# (1, 3): ((1, 1, 1), (1, 2), (2, 1), (3,))
	# (1, 4): ((1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 2), (1, 3), (3, 1), (4,))
  num_permutations = [0, 1, 2, 4, 8]
  # iterate out further with dynamic programming expanding on prior subproblems:
  # each iteration, include 1-width block after all the i-1-width ways,
  # plus 2-width block after all the i-2-width ways, etc. up to the 4-width block
  for i in range(5, m+1):
    num_permutations.append((num_permutations[i - 1] + num_permutations[i - 2] + num_permutations[i - 3] + num_permutations[i - 4]) % modulo)
  
  num_permutations_for_n = [((i ** n) % modulo) for i in num_permutations]
  # intuitively, 0 ways to make a width-0 "good" wall, and only 1 way to make a width-1 "good" wall
  good_permutations = [0, 1]
  # any "good" wall permutation of width < w is essentially one of the "invalid" left portions of a "bad" wall, so we subtract those out, multiplied by the permutations_for_n 
  for i in range(2, m+1):
    gp_for_i = num_permutations_for_n[i]
    for j in range(1, i):
      gp_for_i -= (good_permutations[j] * num_permutations_for_n[i-j])
    good_permutations.append(gp_for_i % modulo)
  return good_permutations[m]

def legoBlocks2(n, m):
    if n < 1 or m < 1:
        return 0
        
    # Special cases for one row (n = 1)
    if n == 1:
        return 0 if m > 4 else 1

    # Initial building blocks configurations for width 1 to 4
    f = [0, 1, 2, 4, 8]

    # Calculate f values up to width m
    for i in range(5, m + 1):
        f.append((f[-1] + f[-2] + f[-3] + f[-4]) % MOD)

    # Compute pn values: number of ways to build n rows with width k
    pn = [pow(f_k, n, MOD) for f_k in f]

    # Compute gn values: number of ways to build a solid wall of width k
    gn = [0, 1]
    for k in range(2, m + 1):
        sum_gp = sum(gn[i] * pn[k - i] for i in range(1, k)) % MOD
        gn.append((pn[k] - sum_gp) % MOD)

    return gn[m]

n = 100
m = 1000

#d = legoBlocks(n, m)
d = pow_mod(999, 1234567890, 13414314515)
e = pow_mod_recursive(999, 1234567890, 13414314515)
f = pow(999, 1234567890, 13414314515)

print(d, e, f)
