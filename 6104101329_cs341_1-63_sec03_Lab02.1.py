# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:26:28 2020

@author: Nutthawut Promboon6104101329
Introduction to Python Lab2

"""
#คาบที่2
#วงเล็บแบบก้างปูเพื่อประกาศตัวแปรหลายชนิด
fam =[1.73,1.68,1.71,1.89]
print(fam)
[1.73, 1.68, 1.71, 1.89]
#ข้อมูลในชุดข้อมูลนี้ แต่ละช่องเรียก element

fam มี 4 element แต่ละ element คั่นด้วย , comma 
list ไม่เหมือนกับ array ในภาษา c

fam = ["lis",1.73,"emma",1.68,"mom",1.71,"dad",1.89]
นั้นคือ list ของ pytron ไม่เหมือน array ของ C เพราะ เป็นโครงสร้างข้อมูล data structure คนละแบบกัน
multi data type 1 dimension
มีข้อมูลภายใน 1 มิติ ของตัวแปร
2 dimension

fam2 = [["lis",1.73],["emma",1.68],["mom",1.71],["dad",1.89]]
print(fam2)
[['lis', 1.73], ['emma', 1.68], ['mom', 1.71], ['dad', 1.89]]

#fam2 คือ ตัวแปร 2 มิติ list ซ้อน list
#fam2 มี 4 element ที่แต่ละ element มี 2 element ย่อย

type(fam2)
Out[32]: list
 
#type 
data type ชนิดของข้อมูลที่เก็บอยู่ในตัวแปร
string int float bool

varlable structure type ชนิดของโครงสร้างข้อมูลตัวแปร
single varlable list

a = 10
b = 20
c = [a,b]


#ใบงานที่1
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
beat = 9.50

areas = [hall,kit,liv,bed,beat]


#ใบงานที่2
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

#ใบงานที่3
house = [["hallway",hall],["kitchan",kit],["living room",liv],["bedroom",bed],["bathroom",beat]]


fam = ['lis',1.73,'emma',1.68,'emma',1.73,'dad',1.89]
ลำดับที่     1    2     3     4     5     6     7    8
ระบบชี้ตำปหน่งที่เริ่มจากเลข 0 เรียกว่า zero-based indexing
        -8   -7    -6    -5    -4    -3    -2   -1                                     
#อยากดึงข้อมูลตำแหน่งที่1
fam[0]
Out[51]: 'lis'
#อยากดึงข้อมูลลำดับที่4
fam[3]
Out[53]: 1.68
#อยากดึงข้อมูลลำดับสุดท้าย idx 7
fam[7]
Out[55]: 1.89


['lis',1.73,'emma',1.68,'emma',1.73,'dad',1.89]
ลำดับที่     1    2     3     4     5     6     7    8
ระบบชี้ตำปหน่งที่เริ่มจากเลข 0 เรียกว่า zero-based indexing
        -8   -7    -6    -5    -4    -3    -2   -1  

fam[-1]
Out[56]: 1.89
fam[-8]
Out[58]: 'lis'

['lis',1.73,'emma',1.68,'emma',1.73,'dad',1.89]
ลำดับที่     1    2     3     4     5     6     7    8
ระบบชี้ตำปหน่งที่เริ่มจากเลข 0 เรียกว่า zero-based indexing
        -8   -7    -6    -5    -4    -3    -2   -1  

การ slicing element ของ list มาเป็นส่วนๆ จะใช้ : colon
start idx : stop idx
fam[3 : 5]
Out[60]: [1.68, 'emma']
1.68 เป็น idx 3 ใน fam 
mom เป็น idx 5 ใน fam

start idx คือเลข 3 inslusion คือเลือกออกมาด้วย 
stop idx คือเลข 5 exelusion คือไม่เลือกออกมา
เลือกข้อมูลตั้งแต่ start idx ไปจนถึง idx ตัวก่อน stop idx
เลือกข้อมูลตั้งแต่ idx 3 ไปจนถึง idx ก่อน 5 (นั้นคือ 4)
fam[1 : 4] #fam idx 1 ไปจนถึง idx ก่อน 4 (นั้นคือ)
Out[61]: [1.73, 'emma', 1.68]
idx        1      2      3 

#กรณีที่ไม่ใส่ตัวเลขหน้าหรือหลัง
fam[4 : ]
Out[62]: ['emma', 1.73, 'dad', 1.89]
การไม่ใส่ : ด้าน stop idx แปลว่า ไปจนสุดท้ายของ list
fam[4 : 8]
Out[63]: ['emma', 1.73, 'dad', 1.89]

ในทางตรงข้าม หน้า : ไม่ใส่ แปลว่า
fam[ : 4]
Out[64]: ['lis', 1.73, 'emma', 1.68]
idx         0     1      2       3

fam[-8 : -1] = fam[0 : 7] idx 0-element

#ใบงานที่4
print(house[1])
['kitchan', 18.0]
print(house[-1])
['bathroom', 9.5]
print(liv)
20.0

#ใบงานที่5
eat_sleep_areas = areas[3] + areas[7]
print(eat_sleep_areas)
28.75

eat_sleep_areas = areas[-7] + areas[-3]
print(eat_sleep_areas)
28.75

#ใบงานที่6
downstairs = areas[0 : 6]
print(downstairs)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
upstairs = areas[6 : ]
print(upstairs)
['bedroom', 10.75, 'bathroom', 9.5]

downstairs = areas[-10 : -4]
print(downstairs)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
upstairs = areas[-4 : ]
print(upstairs)
['bedroom', 10.75, 'bathroom', 9.5]





