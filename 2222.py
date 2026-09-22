import sys
input_data = sys.stdin.read().split()

if not input_data:
    exit()
try:
    line1 = input()
    line2 = input()
except EOFError:
    line1 = ""
    line2 = ""

if not line1:
    print()
    exit()

list1 = list(map(int, line1.split()))
set2 = set(map(int, line2.split())) if line2 else set()

result = []
seen = set()

for num in list1:
    if num not in set2 and num not in seen:
        result.append(num)
        seen.add(num)

print(*result)