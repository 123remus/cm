import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 設定中文顯示（若環境支援）與美化介面
sns.set_theme(style="whitegrid")

def run_advanced_stats_demo():
    # 1. 建立母體 (Population)：假設這是一個非常偏斜的指數分佈 (例如：等待公車的時間)
    # 指數分佈是非常不正態的，長得像滑梯一樣
    population = np.random.exponential(scale=2, size=100000)
    pop_mean = np.mean(population)
    
    # 2. 設定不同的樣本大小 (n) 來觀察變化
    sample_sizes = [2, 10, 50]
    num_simulations = 10000  # 每個實驗重複 1 萬次
    
    plt.figure(figsize=(15, 5))
    
    # 繪製原始母體
    plt.subplot(1, 4, 1)
    sns.histplot(population, bins=50, color='gray', kde=False)
    plt.title(f"Original Population\n(Mean: {pop_mean:.2f})")
    plt.axvline(pop_mean, color='red', linestyle='--') # 標示母體平均值

    # 3. 進行抽樣實驗
    for i, n in enumerate(sample_sizes):
        sample_means = []
        for _ in range(num_simulations):
            # 從母體中隨機抽取 n 個樣本
            sample = np.random.choice(population, size=n)
            sample_means.append(np.mean(sample))
        
        # 繪製不同 n 之後的分佈圖
        plt.subplot(1, 4, i + 2)
        sns.histplot(sample_means, bins=50, kde=True, color='skyblue')
        plt.title(f"Sample Size n = {n}")
        plt.axvline(pop_mean, color='red', linestyle='--')
        plt.xlim(0, 6) # 統一 X 軸範圍方便比較
        
    plt.tight_layout()
    plt.show()

run_advanced_stats_demo()