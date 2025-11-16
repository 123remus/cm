import numpy as np

# c[i] 是 x^i 的係數，例如 f(x) = -5x^4 + 2x^3 + 0x^2 - 3x + 1
c = [1, -3, 0, 2, -5]

# numpy.roots 要的順序是從最高次到最低次，因此要反轉
roots = np.roots(c[::-1])

print("Roots:", roots)
