# 서드파티 API 서버로부터 코인베이스 트랜잭션을 수집해서
# 채굴자의 지급을 관촬. 최근 몇 개의 블록만 조회.

import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

# 마지막 블록 번호를 조회
resp = requests.get(url="https://blockchain.info/latestblock")
data = resp.json()
n_height = data["height"]

# 코인베이스 트랜잭션의 지갑 주소를 수집.
mining = []

for n in range(n_height, n_height - 100, - 1):
    url = "https://blockchain.info/block-height/" + str(n) + "?format=json"
    resp = requests.get(url=url)
    data = resp.json()
    block = data["blocks"][0]

    stime = block["time"]
    addr = block["tx"][0]["out"][0]['script'] # addr -> script로 바뀜.

    value = block["tx"][0]["out"][0]["value"]

    ts = time.gmtime(stime)
    date = time.strftime("%Y-%m-%d %H:%M:%S", ts)

    mining.append([date, addr, value])

    print("#%d : %s\t%s\t%f" % (n, date, addr, value*1e-8))


# 결과 dataframe에 저장
df = pd.DataFrame(mining, columns=["Date", "Address", "Reward"])

# 같은 지갑끼리 바이닝
grp = df.groupby("Address").Address.count()
print()
print(grp)

plt.figure(figsize=(6, 3))
plt.title("Miner's Address")
x = list(range(1, len(grp.values) + 1))
plt.bar(x, grp.values, width=1, color="red", edgecolor="black",
        linewidth=0.5, alpha=0.5)
plt.show()