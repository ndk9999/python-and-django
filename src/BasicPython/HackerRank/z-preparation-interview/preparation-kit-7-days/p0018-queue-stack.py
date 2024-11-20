# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input().strip())

s = []

for _ in range(q):
    cmd = list(map(int, input().strip().split()))
    
    if cmd[0] == 1:
        s.append(cmd[1])
    elif cmd[0] == 2:
        s.pop(0)
    elif len(s) > 0:
        print(s[0])
