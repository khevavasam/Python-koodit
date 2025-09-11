import random

N = int(input())

inside = 0
for _ in range(N):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    if x*x + y*y <= 1.0:
        inside += 1

pi_est = 4.0 * inside / N
print(pi_est)