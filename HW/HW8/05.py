import numpy as np

# ========== 7-4 Hamming Code 編碼 ==========
def hamming74_encode(data_bits):
    """
    data_bits: list of 4 bits, e.g. [1,0,1,1]
    return: 7-bit encoded Hamming code
    """

    d1, d2, d3, d4 = data_bits

    # parity bits
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    # positions 1..7
    code = [p1, p2, d1, p3, d2, d3, d4]
    return code


# ========== 7-4 Hamming Code 解碼（含單一錯誤修正） ==========
def hamming74_decode(code_bits):
    """
    code_bits: 7-bit array
    return: (corrected_code, data_bits)
    """

    c = code_bits.copy()

    # extract bits
    p1, p2, d1, p3, d2, d3, d4 = c

    # syndrome bits
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4

    # syndrome 組成錯誤位置 (二進位)
    error_pos = s1 + (s2 << 1) + (s3 << 2)

    # 若 error_pos != 0：修正該 bit
    if error_pos != 0:
        print(f"偵測到錯誤！錯誤位置 bit = {error_pos}")
        c[error_pos - 1] ^= 1  # flip 該位元

    # extract original data bits
    d1, d2, d3, d4 = c[2], c[4], c[5], c[6]

    return c, [d1, d2, d3, d4]


# ========== 測試 ==========
data = [1, 0, 1, 1]
print("原始資料:", data)

# 編碼
encoded = hamming74_encode(data)
print("編碼結果:", encoded)

# 故意加入單一錯誤（翻轉第 5 位）
received = encoded.copy()
received[4] ^= 1
print("傳輸收到:", received)

# 解碼（自動修正）
corrected, decoded = hamming74_decode(received)
print("修正後:", corrected)
print("解碼出資料:", decoded)
