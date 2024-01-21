import pandas as pd
import matplotlib.pyplot as plt

totalWidth = 0.8               
labelNums = 2                          
barWidth = totalWidth / labelNums
seriesNums = 4

macro_list = ["case", "exchange", "homes", "ikki"]

fast_time = [97.06, 380.57, 137.11, 109.98]
page_time = [60.71, 48.72, 60.28, 48.53]
fast_band = [0, 0, 0, 0]
page_band = [0, 0, 0, 0]

idx = 0
for task in macro_list:
    fast_data = pd.read_csv('./results/macro/' + task + '/fast/latency.csv')
    page_data = pd.read_csv('./results/macro/' + task + '/page/latency.csv')
    fast_x_values = fast_data.iloc[:, 2]
    page_x_values = page_data.iloc[:, 2]

    fast_data = 0
    page_data = 0
    for a in fast_x_values:
        fast_data += a
    for b in page_x_values:
        page_data += b
    
    fast_band[idx] = fast_data / fast_time[idx]
    page_band[idx] = page_data / page_time[idx]
    idx += 1


# fast_latency = [66129, 519376.45, 34652.97, 2699.71, 652552.48, 1222.07]
# page_latency = [66829, 916813.89, 34947.98, 916813.886, 491821.44, 475963.21]
# fast_latency = [53803627, 7737409, 91730258, 1511600, 6182155, 3324482]
# page_latency = [53313412, 4419443, 91128181, 4419443, 8162271, 8428627]

plt.figure(figsize=(8, 6))  # 设置图形尺寸（可选）


plt.bar([x for x in range(seriesNums)], height=fast_band, label="FAST", width=barWidth)
plt.bar([x + barWidth for x in range(seriesNums)], height=page_band, label="PAGE", width=barWidth)

# plt.xticks([x + barWidth / 2 * (labelNums - 1) for x in range(seriesNums)], ["read","write","randread", "randwrite", "readwrite", "randrw"])
# plt.xlabel("Microbenchmark")
# plt.ylabel("Average I/O latency (ns)")
# plt.title("Average I/O latency on microbenchmarks")
# plt.yscale("log")
# plt.legend()
# plt.show()

plt.xticks([x + barWidth / 2 * (labelNums - 1) for x in range(seriesNums)], macro_list)
plt.xlabel("Macrobenchmark")
plt.ylabel("Bandwidth (B/s)")
plt.title("Bandwidth on macrobenchmarks")
# plt.yscale("log")
plt.legend()
plt.show()

plt.savefig("./figs/macro-bandwidth.pdf")