import os
import csv
import datetime
from datetime import datetime

# with open('/Users/mac/Desktop/大學資料/P4CSS-Project_G4/data/all_projects_info_群眾集資_all_var.csv', newline='') as csvfile:
# with open('/Users/mac/Desktop/大學資料/P4CSS-Project_G4/data/all_projects_info_預購式專案_all_var.csv', newline='') as csvfile:
# with open('/Users/mac/Desktop/大學資料/P4CSS-Project_G4/testdata_1_3_預購.csv', newline='') as csvfile:
with open(
    "/Users/mac/Desktop/大學資料/P4CSS-Project_G4/testdata_1_3_募資.csv", newline=""
) as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

    data = []
    # 以迴圈輸出每一列
    for row in rows:
        data.append(row)

# with open('/Users/mac/Desktop/大學資料/P4CSS-Project_G4/fbdata/data_12_25_fb.csv', newline='') as csvfile:
with open(
    "/Users/mac/Desktop/大學資料/P4CSS-Project_G4/募資fb_test.csv", newline=""
) as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

    fb_data = []
    # 以迴圈輸出每一列
    for row in rows:
        fb_data.append(row)

obs = len(data)
# print(data[:2])
tw_digit = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
digit = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
for url in range(1, obs):
    if data[url][21] == "":
        continue
    data[url][21] = data[url][21].replace("年", "")
    data[url][21] = data[url][21].replace("月", "")
    data[url][21] = data[url][21].replace(" ", "/")
    for i in range(12):
        j = 11 - i
        data[url][21] = data[url][21].replace(tw_digit[j], digit[j])
    data[url][21] += "/01"


category = [
    "音樂",
    "攝影",
    "出版",
    "時尚",
    "設計",
    "表演",
    "藝術",
    "科技",
    "教育",
    "遊戲",
    "飲食",
    "空間",
    "社會",
    "插畫漫畫",
    "電影動畫",
    "地方創生",
    "挺好店",
    "新春賀喜",
]
clean_data = []
future_data = []
for i in range(obs):
    # temp = data[i][:2]
    temp = []
    if i == 0:
        temp += ["預購專案", "群眾募資"]
        temp += category
        temp += data[i][3:4]
        temp += ["success"]
        temp += data[i][6:10]
        temp += ["duration"]
        temp += data[i][12:18]
        temp += data[i][19:]
        temp += ["fb讚"]
    else:
        # 把還沒結束的專案去掉
        # if int(data[i][11:12][0][:4]) >= 2022 or (int(data[i][11:12][0][:4]) == 2021 and int(data[i][11:12][0][5:7]) == 12 and int(data[i][11:12][0][8:10]) > 18):
        #   continue

        # if (int(data[i][11:12][0][:4]) == 2021 and int(data[i][11:12][0][5:7]) == 12 and int(data[i][11:12][0][8:10]) > 18):
        #   print(data[i][11:12][0])
        #   future_data.append(i)
        temp += [0, 1]
        for y in category:
            if data[i][2] != y:
                temp.append(0)
            else:
                temp.append(1)
        temp += data[i][3:5]
        temp += data[i][6:10]
        # 將募資時間換成秒
        duration = (
            datetime.strptime(data[i][11:12][0], "%Y/%m/%d %H:%M")
            - datetime.strptime(data[i][10:11][0], "%Y/%m/%d %H:%M")
        ).days + (
            datetime.strptime(data[i][11:12][0], "%Y/%m/%d %H:%M")
            - datetime.strptime(data[i][10:11][0], "%Y/%m/%d %H:%M")
        ).seconds / 86400
        # print(data[i][0])
        # print(data[i][11:12])
        # print(data[i][10:11])
        # print(data[i][21:22])
        # print(duration)
        temp += [duration]
        temp += data[i][12:18]
        temp += data[i][19:21]
        if data[i][21:22][0] == "":
            temp += [None]
        else:
            end_time = (
                datetime.strptime(data[i][21:22][0], "%Y/%m/%d")
                - datetime.strptime(data[i][10:11][0], "%Y/%m/%d %H:%M")
            ).days + (
                datetime.strptime(data[i][21:22][0], "%Y/%m/%d")
                - datetime.strptime(data[i][10:11][0], "%Y/%m/%d %H:%M")
            ).seconds / 86400
            if float(end_time) < 0:
                end_time = 0
            temp += [end_time]
        # print(i)

        temp.append(int(fb_data[i - 1][0]))

    clean_data.append(temp)

# print(len(future_data))

# print(clean_data[:2])
with open("clean_testdata_1_3_募資.csv", "w", newline="") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入另外幾列資料
    for i in range(len(clean_data)):
        writer.writerow(clean_data[i])
