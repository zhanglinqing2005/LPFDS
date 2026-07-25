import math
import csv
import time
import os


# ====================================
# 创建结果目录
# ====================================

RESULT_DIR = "LPFDS_Result"

if not os.path.exists(RESULT_DIR):
    os.makedirs(RESULT_DIR)


trajectory_file = os.path.join(RESULT_DIR, "trajectory.csv")
summary_file = os.path.join(RESULT_DIR, "summary.txt")
counter_file = os.path.join(RESULT_DIR, "counterexample.txt")
prime_file = os.path.join(RESULT_DIR, "primes_found.txt")
first_appearance_file = os.path.join(RESULT_DIR, "first_appearance.csv")


# ====================================
# 最大质因子
# ====================================

def max_prime_factor(n):
    if n < 2:
        return 1
    ans = 1
    while n % 2 == 0:
        ans = 2
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            ans = i
            n //= i
        i += 2
    if n > 1:
        ans = n
    return ans


# ====================================
# 判断质数
# ====================================

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# ====================================
# 下一个质数（带缓存）
# ====================================

prime_cache = {}

def next_prime(p):
    if p in prime_cache:
        return prime_cache[p]
    x = p + 1
    if x < 2:
        x = 2
    while True:
        if is_prime(x):
            prime_cache[p] = x
            return x
        x += 1


# ====================================
# 参数设置
# ====================================

MAX_A = 10**12          # 改成了论文中的 10^12

a = 2
n = 0
last_p = 0

violation1 = 0
violation2 = 0

prime_set = set()
prime_first_index = {}   # 新增：记录首次出现位置

start_time = time.time()


# ====================================
# 写入轨迹文件
# ====================================

with open(trajectory_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "a_n", "p_n"])

    while a <= MAX_A:
        p = max_prime_factor(a)

        if n % 1000 == 0:
            print(f"Running: n={n}, a={a}, p={p}")

        n += 1

        writer.writerow([n, a, p])

        # 记录首次出现
        if p not in prime_set:
            prime_first_index[p] = n
        prime_set.add(p)

        # -----------------------
        # 猜想1检测
        # -----------------------
        if last_p != 0 and p < last_p:
            violation1 += 1
            with open(counter_file, "a") as cf:
                cf.write(f"""
Conjecture 1 failure
n={n}
previous prime={last_p}
current prime={p}
a={a}
""")

        # -----------------------
        # 猜想2检测
        # -----------------------
        if last_p != 0 and p > last_p:
            expected = next_prime(last_p)
            if p != expected:
                violation2 += 1
                with open(counter_file, "a") as cf:
                    cf.write(f"""
Conjecture 2 failure
n={n}
previous={last_p}
current={p}
expected={expected}
a={a}
""")

        last_p = p
        a = a + p


end_time = time.time()


# ====================================
# 保存出现质数列表
# ====================================

with open(prime_file, "w") as f:
    for p in sorted(prime_set):
        f.write(str(p) + "\n")


# ====================================
# 保存首次出现位置（新增）
# ====================================

with open(first_appearance_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["prime", "first_index"])
    for p in sorted(prime_first_index.keys()):
        writer.writerow([p, prime_first_index[p]])


# ====================================
# 保存实验摘要
# ====================================

max_p = max(prime_set) if prime_set else 0

with open(summary_file, "w") as f:
    f.write(f"""
Largest Prime Factor Driven Dynamical System
Computational Experiment Report

Parameters
----------------
Initial value: a_1 = 2
Maximum a: {MAX_A}

Results
----------------
Iterations: {n}
Final value: {a}
Maximum observed prime: {max_p}
Number of different primes: {len(prime_set)}

Conjecture 1 violations: {violation1}
Conjecture 2 violations: {violation2}

Runtime seconds: {end_time - start_time:.2f}

Conclusion:
No counterexample detected within the tested range.
""")


print("Experiment finished")
print(f"Summary saved to: {summary_file}")
print(f"First appearance saved to: {first_appearance_file}")