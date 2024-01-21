import pandas as pd
import matplotlib.pyplot as plt

task_size, task = input().split()

fast_data = pd.read_csv('./results/' + task_size + '/' + task + '/fast/latency.csv')
page_data = pd.read_csv('./results/' + task_size + '/' + task + '/page/latency.csv')

fast_x_values = fast_data.iloc[:, 0]
fast_y_values = fast_data.iloc[:, 3]
page_x_values = page_data.iloc[:, 0]
page_y_values = page_data.iloc[:, 3]

# Initialize an empty list to store the valid points
fast_points = []
page_points = []

# Iterate through the rows of x_values and y1_values
for a, b in zip(fast_x_values, fast_y_values):
    fast_points.append((a, b))
for a, b in zip(page_x_values, page_y_values):
    page_points.append((a, b))

# 提取排序后的 x 和 y 坐标
fast_x = [point[0] for point in fast_points]
fast_y = [point[1] / 1e9 for point in fast_points]
page_x = [point[0] for point in page_points]
page_y = [point[1] / 1e9 for point in page_points]

# 创建折线图
fig, axes = plt.subplots(1, 2, sharex=True, sharey=False, figsize=(16, 6))

# plt.figure(figsize=(8, 6))  # 设置图形尺寸（可选）
axes[0].scatter(fast_x, fast_y, color='r', s = 2, label='FAST')
axes[1].scatter(page_x, page_y, color='b', s = 2, label='PAGE')
axes[0].set_ylim(-100, 2100)
axes[0].set_yticks(range(0, 2200, 200))
axes[1].set_ylim(-100, 2100)
axes[1].set_yticks(range(0, 2200, 200))

# Adding labels, title, and legend
axes[0].set_xlabel('Request (th)')
axes[0].set_ylabel('Latency (ms)')
axes[1].set_xlabel('Request (th)')
axes[1].set_ylabel('Latency (ms)')
# axes[0].set_title('Latency over progress')
# axes[1].set_title('Latency over progress')
axes[0].legend()
axes[1].legend()

# Show the plot
# plt.grid(True)
plt.show()
fig.suptitle('Latency over progress (' + task_size + ": " + task + ')')
plt.savefig("./figs/" + task_size + "-" + task + "-latency.pdf")