import math
import pandas as pd

spl = []  # sample - 표본

# 프로그램 완성 시 삭제.
# spl = [43.40, 43.11, 58.71, 42.96, 53.20, 54.49,
#        47.38, 45.93, 50.37, 48.21, 43.93, 53.29,
#        63.52, 45.05, 58.83, 49.57, 39.91, 43.11,
#        40.78, 41.31, 50.51, 51.28, 67.72, 59.12,
#        55.77, 48.26, 54.91, 44.67, 46.77, 67.59]

# spl = [1.2, 1.1, 0.8, 0.8, 1.8, 1.5, 2.9, 2.7, 3.2, 4.7,
#        1.0, 1.1, 5.7, 7.3, 2.8, 3.3, 2.4, 2.1, 2.5, 3.1,
#        1.0, 1.7, 0.8, 1.0, 3.2, 4.3, 3.0, 5.0, 3.2, 5.5,
#        2.8, 5.5, 3.9, 6.8, 6.7, 7.9, 3.2, 1.3, 0.9, 1.3]

spl = [186, 158, 176, 141, 180, 140, 163, 170, 183, 194,
       165, 175, 176, 172, 175, 180, 158, 180, 176, 178,
       175, 163, 160, 169, 180, 186, 173, 182, 178,
       166, 196, 160, 172, 166, 177, 173, 185, 158, 174,
       150, 140, 178, 187, 172, 174, 174, 156, 186, 178,
       196, 184, 162, 168, 157, 177, 176, 177, 187,
       182, 184, 134, 180, 163, 152, 160, 168, 167,
       188, 135, 179, 192, 166, 171, 184, 172, 155, 137,
       135, 177, 159, 189, 178, 177, 166, 158, 157,
       168, 166, 175, 178, 148, 157, 179, 178, 184, 187,
       158, 154, 143, 155]

n = len(spl)

# n = int(input("표본 개수 입력 : "))
# for i in range(n):
#     temp = float(input("표본 입력(엔터로 구분) : "))
#     spl.append(temp)

xMax = max(spl)
xMin = min(spl)
rng = xMax - xMin  # rng(Range) - 범위
k = math.ceil(float(math.log(n, 2) + 1))  # k는 계급(class)의 수 - Sturge 방식

c = round(rng / k)  # c는 계급구간.

if int(c) % 2 == 0:
    pass
else:
    c = round(c)

cMax = 0
cMin = 0
# 계급 구간 작성.
if round(int(xMax), -1) <= xMax:  # 반올림이 기존보다 작으면 +5
    cMax = round(int(xMax), -1) + 5
elif round(int(xMax), -1) >= xMax:  # 반올림이 기존보다 크면
    cMax = round(int(xMax), -1)

if round(xMin, -1) <= xMin:  # 반올림이 기존보다 작으면
    cMin = round(int(xMin), -1)
elif round(int(xMin), -1) >= xMin:  # 반올림이 기존보다 크면 -5
    cMin = round(int(xMin), -1) - 5

print(cMax, cMin)

cValue = [int(cMin)]  # class value -> 계급값 배열
gap = math.ceil((cMax - cMin) / c)  # 계급구간의 개수
print(gap)

for i in range(gap):
    temp = c + cValue[i]
    cValue.append(temp)
    if cValue[i+1] > cMax:
        cValue[i+1] = cMax
print(list(cValue))
# ============================================================

# 도수 fi 구하기
freq = [0 for i in range(gap)]
for i in range(gap):
    for j in range(len(spl)):
        if cValue[i] <= spl[j] < cValue[i+1]:
            freq[i] += 1
        else:
            pass

# 누적도수(cumulative frequency) Fi 구하기 (재귀함수 표현 가능?)
cf = [0 for i in range(gap)]
cf[0] = freq[0]
for i in range(1, gap):
    cf[i] = cf[i - 1] + freq[i]

# 상대도수(relative frequency) 구하기
rf = [0 for i in range(gap)]
for i in range(gap):
    rf[i] = round((freq[i] / n), 2)


#  누적상대도수 (relative cumulative frequency) 구하기
rcf = [0 for i in range(gap)]
for i in range(gap):
    rcf[i] = round((cf[i] / n), 2)


# 데이터 입력.
c_list = []
for i in range(gap):
    dum = []
    dum.append(cValue[i])
    dum.append("~")
    dum.append(cValue[i+1])  # 여기 아래로 추가되는 값 코딩.
    dum.append(freq[i])
    dum.append(rf[i])
    dum.append(cf[i])
    dum.append(rcf[i])
    c_list.append(dum)

# pandas 를 이용하여 표 출력
df = pd.DataFrame(c_list, columns=["", "계급", "", "도수", "상대도수", "누적도수", "누적상대도수"])  # 값이 추가되면 columns값도 하나 추가.
print(df)




