- [Kafka](#kafka)
  - [Summary](#summary)
  - [Quick Start](#quick-start)
      - [Install](#Install)
  	  - [環境配置](#環境配置)
      - [使用python串接kafka 範例](#使用python串接kafka-範例)
      - [執行結果](#執行結果)
  - [Project Layout](#project-layout)
  - [備註](#備註)


--- 

## Summary

Kafka 介紹

專門在處理「系統跟系統之間的訊息交換」的系統

* 接收訊息（Producer 傳送。

* 儲存訊息（在磁碟裡，安全又快）。

* 傳送訊息給消費者（Consumer 讀取）。

---
名詞解釋

* Producer: 發送訊息的角色，像是你的應用程式。

* Consumer: 接收訊息的角色，像是後台系統、資料分析器。

* Topic: 訊息分類箱，Producer 把訊息送進去，Consumer 從這裡讀出來。

* Broker: Kafka 的伺服器，負責存儲和傳遞訊息。

* Partition: topic 的分片，讓訊息可以分散儲存、平行處理。

* Zookeeper/KRaft: 協調 Kafka 各伺服器運作的元件（新版 Kafka 支援不用 Zookeeper）。

---


## Quick Start

### Install

Step 1. 安裝JDK

* 下載 Java：https://www.oracle.com/java/technologies/downloads/#java8

---

Step 2. 安裝kafka

* 下載Kafka：https://kafka.apache.org/downloads

* 安裝版本： 選擇 Binary downloads

---

Step 3. 安裝zookeeper

* 下載 zookeeper：https://zookeeper.apache.org/releases.html

---

Step 4. 安裝kafka_python

```shell
pip install kafka-python
```

--- 

### 環境配置

啟動 zookeeper
```shell
.\bin\windows\zookeeper-server-start.bat 
```
```shell
.\config\zookeeper.properties
```
--- 

啟動 kafka
```shell
.\bin\windows\kafka-server-start.bat 
```
```shell
.\config\server.properties
```
--- 

### 使用python串接kafka 範例
Producer
```shell
import json
from kafka import KafkaProducer

# 配置 Kafka 連接
producer = KafkaProducer(
    bootstrap_servers=['kafka-forward-cpj-cqa.ljbrsrc.site:8000', 
                       'kafka-forward-cpj-cqa.ljbrsrc.site:8001', 
                       'kafka-forward-cpj-cqa.ljbrsrc.site:8002'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 將訊息序列化成 JSON 並編碼為 bytes
)

# 構建 JSON 訊息
message = {
    "RoomId": "1056_2_8_15224",
    "Message": "dc201_0422 send", 
    "MessageType": 1,               # 1:訊息 2:曬單
    "Name": "dc201_brentmainadd ",
    "NickName": "dc201nickname",
    "VipLevel": 3,                  # vip:{1~10}
    "IsSteamer": True,             # True:主播 False:非主播
    "Platform": "dc201",            # 平台:dc201(dev/cqa)
    "TimeStamp": 1745223482
}

# 發送消息到 Kafka
#'sync-steaming-message-dc201',  # 指定主題名稱(主>外 直播間訊息傳送)
#'receive-steaming-message-dc201',  # 指定主題名稱(外>主 直播間訊息傳送)
producer.send('receive-steaming-message-dc201', value=message)
producer.flush()
producer.close()

print("Message sent successfully.")

```
Consumer
```shell
from kafka import KafkaConsumer

# 配置 Kafka 連接
consumer = KafkaConsumer(
    'sync-steaming-message-dc201',  # 指定主題名稱(主>外 直播間訊息傳送)
    #'receive-steaming-message-dc201',  # 指定主題名稱(外>主 直播間訊息傳送)
    bootstrap_servers=['kafka-forward-cpj-cqa.ljbrsrc.site:8000', 
                       'kafka-forward-cpj-cqa.ljbrsrc.site:8001', 
                       'kafka-forward-cpj-cqa.ljbrsrc.site:8002'],  # Kafka Broker 列表
    group_id='my-consumer-group',  # 消費者群組 ID，這是用來管理多個消費者的
    auto_offset_reset='earliest',  # 設置從哪裡開始消費，'earliest' 表示從最早的消息開始
    enable_auto_commit=True,  # 啟用自動提交偏移量
    value_deserializer=lambda x: x.decode('utf-8')  # 消費的消息會是字節流，我們把它解碼成 UTF-8 字符串
)

# 消費消息
print("開始從 Kafka 主題消費消息...")
for message in consumer:
    print(f"接收到消息: {message.value}")
    # 可以在這裡處理消息，進行其他操作

```
---
### 執行結果
Producer
```shell
Message sent successfully.
```
Consumer
```shell
開始從 Kafka 主題消費消息...
接收到消息: {"RoomId": "1056_2_8_15224", "Message": "dc201 send", "MessageType": 1, "Name": "dc201_brentmainadd ", "NickName": "", "VipLevel": 3, "IsSteamer": true, "Platform": "dc201", "TimeStamp": 1745223482}
```

---

## Project Layout

```text
Pytest
 ├─ README.md            #
 |─ src                  # 主程式
      ├─ Consumer.py     # 接收端範例程式
      ├─ Producer.py     # 發送端範例程式


```

---

## 備註
1. 新版Kafka不需zookeeper。
2. Offset Explorer 3.0 為kafka工具，主要為Consumer角色，可確認數據。

   下載: https://www.kafkatool.com/download.html

---
