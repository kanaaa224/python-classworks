import numpy as np
import matplotlib.pyplot as plt

# 角度を0〜360度で1度刻みで作成
angles = np.arange(0, 361, 1) # 360とすると360度が含まれない

# 角度をラジアンに変換
radians = np.deg2rad(angles)

# sinとcosの値を計算
sin_values = np.sin(radians) * 1.5 # sin値を1.5倍
cos_values = np.cos(radians) * 2.0 # cos値を2.0倍

# 2次元配列にまとめる（列: sin, cos）
values_array = np.column_stack((sin_values, cos_values))

# コンソール出力
np.set_printoptions(precision=3, suppress=True)
print("角度ごとの sin, cos の値（ sin * 1.5, cos * 2.0 ）:")
print(values_array)

# グラフの描画
plt.figure(figsize=(10, 5))
plt.plot(angles, sin_values, label='sin*1.5', color='blue')
plt.plot(angles, cos_values, label='cos*2.0', color='red')
plt.title('Sin and Cos Values')
plt.xlabel('Angle (degrees)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()