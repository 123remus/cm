import numpy as np

def cross_entropy(P, Q):
    P = np.array(P, dtype=float)
    Q = np.array(Q, dtype=float)
    mask = (P > 0) & (Q > 0)
    return -np.sum(P[mask] * np.log(Q[mask]))

def random_distribution(n):
    """產生隨機機率分佈"""
    x = np.random.rand(n)
    return x / x.sum()

# 驗證多組 p, q
for _ in range(10):
    p = random_distribution(5)      # 產生 p
    q = random_distribution(5)      # 產生 q (大多數情況 ≠ p)

    ce_pp = cross_entropy(p, p)
    ce_pq = cross_entropy(p, q)

    print("p =", p)
    print("q =", q)
    print("H(p,p) =", ce_pp)
    print("H(p,q) =", ce_pq)
    print("H(p,p) < H(p,q)?", ce_pp < ce_pq)
    print("-" * 50)
