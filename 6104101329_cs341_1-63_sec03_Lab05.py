# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:16:30 2020
@author: Nutthawut Promboon6104101329 cs341 sec03
Python Lab5
"""

อยากเรียกใช้ package ใดๆ ก็ import
import pandas as pd
#ModuleNotError : No module name 'pandas'
#ให้กลับไปดูว่า run บน enviroment ที่ลง panda package หรือยัง
#Anaconda Navigator เช็ค installed pakage
#ไปดูคลิปย้อนหลังใน MS Team

import pandas as pd

dict = {'country':['Brazil','Russia',
                   'India','China',
                   'South Africa'],
        'captial':['Brazillia','Moscow',
                   'New Delhi','Beijin',
                   'Pretoria'],
        'area':[8.5616,17.10,3.286,9.597,1.221],
        'population':[200.4,143.5,1252,1357,52.58]
        }

เราสร้าง Dictionary ชื่อ dict เก็บข้อมูลที่เราอยากแปลงเป็น dataframe
ถ้าเราอยากสร้าง dataframe เราจะไปยืม method จาก pd
pd object pandas

brics = pd.DataFrame(dict)
เราจะสร้าง dataframe ชื่อ brics โดยเรียกใช้ method ชื่อ DataFrame
ซึ่งเป็นของ object pd แล้วป้อนข้อมูลใน dict เป็น argument
print(brics)
        country    captial     area  population
0        Brazil  Brazillia   8.5616      200.40
1        Russia     Moscow  17.1000      143.50
2         India  New Delhi   3.2860     1252.00
3         China     Beijin   9.5970     1357.00
4  South Africa   Pretoria   1.2210       52.58

จะเห็นว่า key ของ dict จะถูกเอามาทำเป็นชื่อ colum  colum label
แต่ในส่วนของ ชื่อของแต่ละแถว row label เรายังเห็นเป็นเลข index 0-4

เราสามารถที่จะ ทำ row label เป็นอักษรได้ ไม่ต้องเป็นเลข index 


alpha = ['BR','RU','IN','CH','SA']
brics เป็น pandas datafram obj
ดังนั้นมันจะมี method attribute เป็นของตัเอง
brics.index = alpha
print(brics)
         country    captial     area  population
BR        Brazil  Brazillia   8.5616      200.40
RU        Russia     Moscow  17.1000      143.50
IN         India  New Delhi   3.2860     1252.00
CH         China     Beijin   9.5970     1357.00
SA  South Africa   Pretoria   1.2210       52.58

จะสร้างตัวแปร brics2 ที่รับข้อมูลจากการอ่านไฟล์ brics.csv ด้วย
Method ของ pd
brics2 = pd.read_csv('brics.csv')
print(brics2)
Unnamed: 0       country    capital    area  population
0         BR        Brazil   Brasilia   8.516      200.40
1         RU        Russia     Moscow  17.100      143.50
2         IN         India  New Delhi   3.286     1252.00
3         CH         China    Beijing   9.597     1357.00
4         SA  South Africa   Pretoria   1.221       52.98

จะเห็นว่ายัง import มาผิด colum แรก อยากให้เป็น index

brics2 = pd.read_csv('brics.csv',index_col = 0)
print(brics2)
         country    capital    area  population
BR        Brazil   Brasilia   8.516      200.40
RU        Russia     Moscow  17.100      143.50
IN         India  New Delhi   3.286     1252.00
CH         China    Beijing   9.597     1357.00
SA  South Africa   Pretoria   1.221       52.98

index_col คือการบอก read_csv ว่า col หมายเลขใดจะเป็น row label

------------------------------------------------------------
 
ใบงานที่1
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
dr=  [True, False, False, False, True, True, True]
cpc= [809, 731, 588, 18, 200, 70, 45]

import pandas as pd



my_dict = {'country':names,'drive_right':dr,'car_per_car':cpc}
cars = pd.DataFrame(my_dict)

row_labels = ["US","AUS","JAP","IN","RU","MOR","EG"]

car เป็น datafram object ดังนั้น cars จึงได้รับ inherits
car.index = row_labels


ใบงานที่2
ให้ load ข้อมูลใน cars.csv มาเก็บในตัวแปร datafram ชื่อ cars2
ให้ลองคลิกเปิด cars.csv ด้วย ms excel ดูดีๆว่า
column แรกเป็น index ไม่ใช่ข้อมูล
ดังนั้นแล้ว ตอน read อย่าลืม set index column
cars2 = pd.read_csv('cars.csv', index_col=0)

#ความเป็นจริง เราจะไม่ได้ทำงานกับข้อมูลทั้งหมด
#เราเลือก select ออกมาเฉพาะบางส่วนของ dataframe
#[] : เราเลือกเฉพาะบางแถว
อยากได้ประเทศ1ไปจนถึง5
cars2[0:5] # 0 1 2 3 4 ไม่เลือกประเทศ idx5
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False
IN             18          India         False
RU            200         Russia          True

ใบงานที่3
เลือกออกมา 3 แถวแรก
cars2[0:3]
     cars_per_cap        country  drives_right
US            809  United States          True
AUS           731      Australia         False
JAP           588          Japan         False

เลือกออกมาแถวที่ 4 5 6 
cars2[4:7]
     cars_per_cap  country  drives_right
RU            200   Russia          True
MOR            70  Morocco          True
EG             45    Egypt          True

เลือก 2 แถวสุดท้าย
cars2[-2:]
     cars_per_cap  country  drives_right
MOR            70  Morocco          True
EG             45    Egypt          True

#ในข้อ 3 เราเลือกเฉพาะ แถวแบบ index เป็นตัวเลข
#เราสามารถเชื่อมต่อ ที่เรา set ให้เป็น index ได้
#เช่น United State เราย่อ US
แต่เราจะเรียกแบบอักษรย่อได้ต้องไป call method.loc
cars2.loc['US']
cars_per_cap              809
country         United States
drives_right             True
Name: US, dtype: object

type(cars2.loc['US']) #พิมพ์ชนิดผลลัพธ์การ loc ออกมา
pandas.core.series.series

cars2.loc[['US']]
    cars_per_cap        country  drives_right
US           809  United States          True

type(cars2.loc[['US']])
pandas.core.frame.DataFrame

#ถ้าอยากจะตัดข้อมูลแถวใน dataframe.loc[[]]
#loc ย่อมาจาก location

cars2.loc[['US',"JAP"]]
     cars_per_cap        country  drives_right
US            809  United States          True
JAP           588          Japan         False

แต่ถ้าข้อมูลทำ index ด้วยตัวเลข แล้วอยากอ้างถึงแบบตัวเลข
.iloc
cars2.iloc[[0,2]]
     cars_per_cap        country  drives_right
US            809  United States          True
JAP           588          Japan         False


ใบงานที่4
บังคับใช้ loc ได้ข้อมูลออกมาเป็น dataframe
อยากตัดข้อมูลออกเฉพาะ ประเทศ Morocco
cars2.iloc[[5]]
     cars_per_cap  country  drives_right
MOR            70  Morocco          True

อยากได้ข้อมูลเฉพาะ ประเทศ อินเดีย กับ รัสเซีย
cars2.iloc[[3,5]]
     cars_per_cap  country  drives_right
IN             18    India         False
MOR            70  Morocco          True



















