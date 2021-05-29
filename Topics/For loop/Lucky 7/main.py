int_num = int(input())
ints = []
for _ in range(int_num):
    ints.append(int(input()))

for num in ints:
    if num % 7 == 0:
        print(num ** 2)
