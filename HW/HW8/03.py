import numpy as np

def entropy(P):
    """
    熵 H(P) = - Σ p(x) log p(x)
    """
    P = np.array(P, dtype=float)
    P = P[P > 0]  # 避免 log(0)
    return -np.sum(P * np.log(P))


def cross_entropy(P, Q):
    """
    交叉熵 H(P, Q) = - Σ p(x) log q(x)
    """
    P = np.array(P, dtype=float)
    Q = np.array(Q, dtype=float)
    mask = (P > 0) & (Q > 0)  # 避免 log(0)
    return -np.sum(P[mask] * np.log(Q[mask]))


def kl_divergence(P, Q):
    """
    KL 散度 D(P || Q) = Σ p(x) log (p(x) / q(x))
    """
    P = np.array(P, dtype=float)
    Q = np.array(Q, dtype=float)
    mask = (P > 0) & (Q > 0)
    return np.sum(P[mask] * np.log(P[mask] / Q[mask]))


def mutual_information(joint_P):
    """
    互資訊 I(X;Y) = Σ p(x,y) log (p(x,y) / (p(x)p(y)))
    joint_P: 二維 joint distribution，例如：
       [[0.1, 0.2],
        [0.3, 0.4]]
    """
    joint_P = np.array(joint_P, dtype=float)

    # 邊際分布
    PX = joint_P.sum(axis=1)   # P(x)
    PY = joint_P.sum(axis=0)   # P(y)

    I = 0.0
    for i in range(joint_P.shape[0]):
        for j in range(joint_P.shape[1]):
            pxy = joint_P[i, j]
            if pxy > 0:
                I += pxy * np.log(pxy / (PX[i] * PY[j]))

    return I


# ======== 測試範例 ========

P = [0.2, 0.5, 0.3]
Q = [0.3, 0.4, 0.3]

joint = [
    [0.1, 0.2],
    [0.3, 0.4]
]

print("Entropy H(P) =", entropy(P))
print("Cross Entropy H(P, Q) =", cross_entropy(P, Q))
print("KL Divergence D(P||Q) =", kl_divergence(P, Q))
print("Mutual Information I(X;Y) =", mutual_information(joint))
