import numpy as np
import matplotlib.pyplot as plt

def simulate_clt(population_type='uniform', sample_size=30, num_samples=10000):
    """
    模擬中央極限定理
    :param population_type: 原始總體的分佈類型 ('uniform' 或 'exponential')
    :param sample_size: 每次抽樣的樣本數 (n)
    :param num_samples: 抽樣次數
    """
    
    # 1. 產生原始總體數據 (非正態分佈)
    if population_type == 'uniform':
        data = np.random.uniform(1, 10, 100000)
        title_prefix = "Uniform"
    else:
        data = np.random.exponential(scale=1.0, size=100000)
        title_prefix = "Exponential"

    # 2. 進行多次抽樣並計算每次的平均值
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(data, size=sample_size)
        sample_means.append(np.mean(sample))

    # 3. 繪圖可視化
    plt.figure(figsize=(12, 5))

    # 左圖：原始數據的分佈
    plt.subplot(1, 2, 1)
    plt.hist(data, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(f"Original {title_prefix} Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # 右圖：樣本平均值的分佈 (預期呈現鐘形曲線)
    plt.subplot(1, 2, 2)
    plt.hist(sample_means, bins=50, color='salmon', edgecolor='black', alpha=0.7)
    plt.title(f"Distribution of Sample Means (n={sample_size})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

# 執行模擬：從均勻分佈中抽取樣本
simulate_clt(population_type='uniform', sample_size=30, num_samples=10000)
