import matplotlib.pyplot as plt

totalWidth = 0.8               
labelNums = 2                          
barWidth = totalWidth / labelNums
seriesNums = 6

# fast_latency = [66129, 519376.45, 34652.97, 2699.71, 652552.48, 1222.07]
# page_latency = [66829, 916813.89, 34947.98, 916813.886, 491821.44, 475963.21]
fast_latency = [53803627, 7737409, 91730258, 1511600, 6182155, 3324482]
page_latency = [53313412, 4419443, 91128181, 4419443, 8162271, 8428627]

plt.figure(figsize=(8, 6))  # 设置图形尺寸（可选）


plt.bar([x for x in range(seriesNums)], height=fast_latency, label="FAST", width=barWidth)
plt.bar([x + barWidth for x in range(seriesNums)], height=page_latency, label="PAGE", width=barWidth)

# plt.xticks([x + barWidth / 2 * (labelNums - 1) for x in range(seriesNums)], ["read","write","randread", "randwrite", "readwrite", "randrw"])
# plt.xlabel("Microbenchmark")
# plt.ylabel("Average I/O latency (ns)")
# plt.title("Average I/O latency on microbenchmarks")
# plt.yscale("log")
# plt.legend()
# plt.show()

# plt.xticks([x + barWidth / 2 * (labelNums - 1) for x in range(seriesNums)], ["case", "exchange", "homes", "ikki"])
plt.xticks([x + barWidth / 2 * (labelNums - 1) for x in range(seriesNums)], ["read","write","randread", "randwrite", "readwrite", "randrw"])
plt.xlabel("Microbenchmark")
plt.ylabel("Bandwidth (B/s)")
plt.title("Bandwidth on microbenchmarks")
# plt.yscale("log")
plt.legend()
plt.show()

plt.savefig("./figs/micro-bandwidth.pdf")