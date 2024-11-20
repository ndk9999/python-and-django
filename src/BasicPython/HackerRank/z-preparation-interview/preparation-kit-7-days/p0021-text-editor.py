# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input().strip())
s = ''
cb = []

for _ in range(q):
    cmd = input().strip().split()
    x = int(cmd[0])
    
    if x == 1:
        cb.append(s)
        s += cmd[1]
    elif x == 2:
        cb.append(s)
        s = s[:len(s)-int(cmd[1])]
    elif x == 3:
        print(s[int(cmd[1]) - 1])
    else:
        s = cb.pop()
