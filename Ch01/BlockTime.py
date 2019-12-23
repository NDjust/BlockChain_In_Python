# 채굴자에 의해 블록이 생성되는 시간 간격을 관찰.
# 블록이 생성되는 시간 간격은 지수분포를 따르므로
# 내 거래가 몇 분 이내에 채굴될 확률이 얼마인지 계산.

import requests
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("금일 생성된 블록을 읽어옵니다.")

url = "https://blockchain.info/blocks?format=json"
resp = requests.get(url=url)
data = resp.json()

header = []
block = data['blocks']
for n in range(len(block)):
    height = block[n]['height']
    btime = block[n]['time']
    bhash = block[n]['hash']
    header.append([header, btime, bhash])

# 어제 생성된 블록을 읽어 온다.
stime = btime - 24 * 60 * 60

# 이전 10일 동안 생성된 블록 정보를 읽어온다.
for n_day in range(0, 10):
    ts = time.gmtime(stime)
    date = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    print("%s 생성된 블록을 읽어옵니다." % date)

    url = "https://blockchain.info/blocks/" + str(stime) + "000?format=json"
    resp = requests.get(url=url)
    data = resp.json()

    block = data["blocks"]

    for n in range(len(block)):
        height = block[n]["height"]
        btime = block[n]["time"]
        bhash = block[n]["hash"]
        header.append([height, btime, bhash])

    stime = block[0]["time"] - 24 * 60 * 60

df = pd.DataFrame(header, columns=["Height", "Time", "Hash"])
sdf = df.sort_values("Time")
sdf = sdf.reset_index()

print("총 %d 개 블록 헤더를 읽어왔습니다." %len(df))

# 블록 생성에 소요되는 시간 분포 관찰.
mtime = sdf["Time"].diff().values
mtime = mtime[np.logical_not(np.isnan(mtime))]
print("평균 Mining 시간  = %d (초)" % np.mean(mtime))
print("표준편차 = %d (초)" % np.std(mtime))

plt.figure(figsize=(8, 4))
n, bins, patches = plt.hist(mtime, 30, facecolor="red", edgecolor="black",
                            linewidth=0.5, alpha=0.5)
plt.title("Mining Time Distribution")
plt.show()

# 5분 이내에 내 거래가 채굴될 확률
s = 60 * 5
p = 1 - np.exp(-s / np.mean(mtime))
print("5분 이내에 내 거래가 Mining될 확률 = %.2f (%s)" % (p * 100, '%'))