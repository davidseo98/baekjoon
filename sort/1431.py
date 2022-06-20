import sys

n = int(sys.stdin.readline().rstrip())
serial_codes = list()
for _ in range(n):
    code = sys.stdin.readline().rstrip()
    num_sum = 0
    for l in code:
        if l.isnumeric():
            num_sum += int(l)
    serial_codes.append((code, num_sum))

serial_codes.sort()
serial_codes.sort(key=lambda x: x[1])
serial_codes.sort(key=lambda x: len(x[0]))

for code in serial_codes:
    print(code[0])
