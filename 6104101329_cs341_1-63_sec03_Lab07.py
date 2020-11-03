# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:04:34 2020
@author: Nutthawut Promboon6104101329 cs341 sec03
Python Lab7
"""


import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, pop)
plt.show()

plt.scatter(year, pop)
plt.show()

# -------------------------------------

# เราจะ load ข้อมูลที่อยู่ใน file year_pop.csv อย่างไร
# ใน lab05 เราเรียนรู้เกี่ยวกับ library สำหรับจัดข้อมูลเชิงตารางราง
# pandas
import pandas as pd
yp_df = pd.read_csv('year_pop.csv')
# .columns มีความหมายว่า ให้แสดงชื่อ ของ column ของ dataframeนี้

yp_df.columns
Out[8]: Index(['year', 'pop'], dtype='object')

# .describe คือ method ที่แสดงค่าสถิติเบื้องต้น
# ของแต่ละ colymn ใน df
yp_df.describe()
Out[9]: 
              year         pop
count   151.000000  151.000000
mean   2025.000000    7.491391
std      43.734045    2.719258
min    1950.000000    2.530000
25%    1987.500000    5.095000
50%    2025.000000    8.080000
75%    2062.500000   10.045000
max    2100.000000   10.850000

# ถ้าอยากดึง Select เอาเฉพาะ year column ออกมาจาก dataframe
yp_df['year']
yp_df.loc[:, 'year']
yp_df.iloc[:, 0]

# อยากเลือก pop column มาเก็บใน pop สั่งอย่างไร
pop = yp_df['pop']
year = yp_df['year']

# หลังจากนี้คือ การวาดกราฟเชิงเส้น ด้วยแกน x คือ ปี และแกน y คือ จำนวนประชากร
import matplotlib.pyplot as plt
plt.plot(year, pop)
plt.show()
บนจอด้านขวา แสดงการเพิ่มขึ้นของจำนวนประชากรในแต่ละปี
ตั้งแต่ปี1950-2100
เป็นกราฟเชิงเส้น แต่ไม่ได้เป้นกราฟเส้นตรง (linear linear)
s curve

# ใบงานที่2 read gapminder.csv
# มาเก็บในตัวแปร gapminder_df
# แต่อย่าลืมว่า ข้อมูลcolumn แรกใน csv ไม่ใช่ dataframe
# แต่เป็น imdex
# read แบบนี้ไม่ใช้ข้อมูล df โครงสร้างอย่างที่ต้องการ
# เราต้องการให้ column แรกเป็น index
gapminder_df = pd.read_csv('gapminder.csv')
# ต้องสั่งแบบนี้
gapminder_df = pd.read_csv('gapminder.csv',index_col = 0)

อ่านเฉพาะ column life_exp มาไว้ในตัวแปร life_exp
life_exp = gapminder_df['life_exp']
อ่านเฉพาะ column gdp_cap มาไว้ในตัวแปร gdp_cap
gdp_cap = gapminder_df['gdp_cap']

ปฟติพอเรา Select มาบาง column มาเก็บชอบดูว่า ข้อมูลเป็นแบบไหน
.head   .tail
life_exp.head()
Out[32]: 
11    43.828
23    76.423
35    72.301
47    42.731
59    75.320
Name: life_exp, dtype: float64

life_exp.tail()
1655    74.249
1667    73.422
1679    62.698
1691    42.384
1703    43.487
Name: life_exp, dtype: float64

วาดแผนภูมิเชิงเส้น ที่ให้แกน x เป็น gdp และ y เป็น life_exp
plt.plot(gdp_cap, life_exp)
plt.show()

# จะเห็นได้ว่าแผนภูมิเส้นไม่สาามารถอธิบายข้อมูลได้
# ต้องไปใช้แผนภูมิแสดงกรกระจายข้อมูล scatter plot
plt.scatter(gdp_cap, life_exp)
plt.show()
# แกน x สัดส่วนตัวเลข scale
# จะเพิ่มทีละ 10000 จาก 0 ไป 50000
# แบบนี้เรียกว่า scale เพิ่มแบบ linear สัดส่วนคงที่
# มันทำให้ดูข้อมูลยาก จะเห็นว่า จุดของแต่ละประเทศมันซ้อนกันที่ช่วง
# 0-10000
# เราสามารถ คลี่ขยาย scale แกฟน x เป็นแบบเพิ่มทวีคูณได้
# เราเรียกว่า log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.yscale('log')
plt.show()

ใบงานที่4 เปลี่ยนแกน x เป็น
population column/1000000
ได้ในตัวแปร pop 
Select population ออกมาหาร 1 ล้าน
pop = gapminder_df['population']/1000000
วาด Select
plt.scatter(pop, life_exp)
plt.xscale('log')
# plt.yscale('log')
plt.show()

แกน x เพิ่มแบบ สิบ ร้อย พัน
จากแผนภูมิ scatter ระหว่าง จำนวนประชากร กับ ดัชชนีสุขภาพ
นศ คิดว่า ประชากรมีนัยยะกับดัชนีสุขภาพหรือไม่
มีนัยยะ ประชากรเพิ่ม สุขภาพดี
ประชากรน้อย สุขภาพแย่
มีนัยยะ
เพราะ
กราฟช่วงหลัง มีสุขภาพดีขึ้น

# Histogram แผนภูมิความถี่ข้อมูลในแต่ละช่วงข้อมูล

ใบงานที่5 
plt.hist(life_exp, bins=10)
plt.show()
นักศึกษาคิดว่า ช่วงตัวเลขดัชนีสุขภาพที่ประมาณเท่าไหร่
ที่มีจำนวนประเทศมากที่สุด
ช่วงตัวเลข life_exp 70-73 คือ bin ที่ 8
จะมีจำนวนประเทศมากที่สุด
ประมาณ 30 ประเทศ

plt.hist(life_exp, bins=20)
plt.show()

plt.hist(life_exp, bins=30)
plt.show()

plt.hist(gdp_cap, bins=10)
plt.show()

plt.hist(gdp_cap, bins=30)
plt.show()

อยากให้นักศึกษาเห็นถึงความแตกต่างของการเพิ่ม bin()
ยิ่งเพิ่มเยอะ ยิ่งเห็นรายละเอียด

plt.hist(life_exp)
plt.show()
argument bins = ใช้ default 10

ใบงานที่7
life_exp1950 = pd.read_csv('life_exp1950.csv')
l_ex1950 = life_exp1950.iloc[:, 0]
plt.hist(l_ex1950, bins=15)

plt.hist(life_exp1950.iloc[:, 0], bins=15)
plt.show()

life_exp1950.describe()

plt.hist(life_exp, bins=15)
plt.show()

จาก Histogram ของดัชนีสุขภาพ
ปี 1950 และ ปี 2007
นักศึกษาคิดว่า สุขภาพของคนบนโลกนี้ ดีขึ้นหรือไม่
ดึขึ้น
อธิบายเหตุผล
เพราะกราฟของปี 2007 ช่วง 70-72.5 ดัชนีสุขภาพสูงกว่าปี 1950

import pandas as pd
import matplotlib.pyplot as plt

plt.ploy(gdp_cap, life_exp)

# ใบงานข้อที่9เติมข้อมูล attribute population เข้าไปในกราฟ
# ให้กลายเป็น มิติที่3
# population ข้อมูลประชากร หลักล้าน ต้องแปรตัวเลขให้ง่าย
pop = gapminder_df['population']/1000000

# ใบงานี่10 เติมข้อมุล attribute color เข้าไปในกราฟ
# ให้ลายเป็นมิติที่ 4 ของการนำเสนอข้อมูล
# color แทนสีของประเปศนั้้นๆ ตั้งอยู่
col = gapminder_df['color']

# ค่าแม่สี #FFFFF

# ----------------------------------
#ploy scatter set x axis scale is logerithm
# x เป็น gdp_cap y เป็ย life_exp และให้ size เป็น pop
# color เป็น col
plt.scatter(gdp_cap, life_exp, s = pop, c = col, alpha = 0.7)
plt.xscale('log')
#set axis name
plt.xlabel('GDP per Capita [in USD')
ylab = 'Life Expectency [in years'
plt.ylabel(ylab)
# ใบงานที่7 อยากให้เรา ตั้งชื่อของ กราฟว่า World Development in 2007
# ชื่อของกราฟว่า title
plt.title('World Development in 2007')
# อยากจะใส่ตัวบอกระยะ ticks แกน x
# เป็นตัวเลข 1000 10000 100000 แล้วสัญลักณ์ 1,000 10,000 100,000
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_lab)
# ถ้าอยากใส่ตัวบอกระยะ ticks แกน y
# เป็นตัวเลข 40 60 80 สัญลักษณ์ 40B 60B 80B
# plt.show()


# ถ้าอยากใส่ตัวบอกระยะ ticks แกน y
# เป็นตัวเลข 40 60 80 สัญลักษณ์ 40B 60B 80B
# plt.scatter(gdp_cap, life_exp)
# plt.xscale('log')
# plt.xlabel('GDP per Capita [in USD')
# ylab = 'Life Expectency [in years'
# plt.ylabel(ylab)
# plt.title('World Development in 2007')
tick_val = [40, 60, 80]
tick_lab = ['40B', '60B', '80B']
plt.yticks(tick_val, tick_lab)

# เราสามารถใส่ข้อความ ด้วยmethod.text
plt.text(1550,71,'India')
# ใครรู้วิธีวนรอบก็ไปวนรอบ
plt.show()











