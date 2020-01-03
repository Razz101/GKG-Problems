import math


def count9divisors(m):
    res_count = 0

    for k in range(m, 35, -1):
        cnt = 0
        root = math.sqrt(k)
        if int(root + 0.5)**2 == k:
            x = int(root) + 1
            for i in range(1, x):
                if k % i == 0:
                    if k / i == i:
                        cnt = cnt + 1
                    else:
                        cnt = cnt + 2
            if cnt == 9:
                res_count += 1
    print(res_count)


n = int(input())
numbers = [int(input()) for _ in range(n)]
for num in numbers:
    count9divisors(num)
