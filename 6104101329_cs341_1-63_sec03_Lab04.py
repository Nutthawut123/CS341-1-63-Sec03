# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:06:48 2020
@author: Nutthawut Promboon6104101329 cs341 sec03
Introduction to Python Lab4
"""

สร้างตัวแปร list ชื่อ pop ไว้เก็บข้อมูลประชากร 3 ประเภท
(pop population ประชากร)
list ใช้ สัญลักษณ์ [] square bracket
pop = [30.55,2.77,39.21]
สร้างตัวแปร list ชื่อ countries ไว้เก็บข้อมูลชื่อประเทศ 3 แระเทศ
countries = ["afghanistan",
             "albania",
             "algeria"]

ถ้าเราอยากรู้ว่า ประชากรในประเทศ albania มีกี่คน
เราต้องไปค้นก่อนว่า albania คือ index หมายเลขใดใน countries
เอาเลข index นั้นมา select ใน pop เพื่อให้ได้ประชากร
ind_alb = countries.index("albania")
#ind_alb จะได้ค่าเลข 1 ออกมา
#คือ index ของคำว่า albania ใน countries
print(pop[ind_alb])
2.77
#พิมพ์ค่า ของ pop ในตำแหน่งที่ ind_alb (คือ ๅ) ออกมา
#วิธีการที่ทำไปนี้ เป็นวิธีการแบบเก่า
#ใช้ list แทน attribute ทีละ attribute
#ค้น index จากชื่อประเทศ แล้วเอา index ไปค้นข้อมูล attributr ต่อไม่ค่อยสะดวก

จึงมีการพัฒนา ตัวแปรโครงสร้างแบบ Dictionary
Dictionary ประกอบด้วย
คำศัพท์ (key) และ ความหมายของคำศัพท์ (value) และคั่นด้วย : colon
เป็นแต่ละ element ใน Dictionary
การสร้าง Dictionary ใช้สัญลักษณ์ {} วงเล็บปีกกา ครอบข้อมูล
world = {"afgahnistan":30.55,
         "albania":2.77,
         "algeria":39.22}
Dictionary เป็นตัวแปรชุด ที่มีข้อมูลหลายๆ element เก็บอยู่
แต่ละ element ประกอบด้วย key และ value นั้นด้วย :
เรา construct ตัวแปร world เป็น Dictionary
และ assign ข้อมูลลงไป 3 element

เราต้องการเข้าถึงข้อมูลเพื่อเลือกข้อมูลออกมา (access, select)
world['albania']    
Out[7]: 2.77
เราเรียกตัวแปร Dictionary ใช้สัญลักษณ์ [] ป้อนชื่อ key ที่ต้องการ value

world['algeria']
Out[8]: 39.22
กรณี access แล้วใส่ key ที่ไม่มีใน Dictionary
world['afcahnstain']
KeyError: 'afcahnstain'

dict_name[key] ก็จะได้ value ของ key

page 5
world = {"afgahnistan":30.55,
         "albania":2.77,
         "algeria":39.22,
         "sealand":2.7e-05}
#e-05 x*0.00001 10^-5
2.7e-05 = 0.0000027

แต่เราได้ข้อมูลเพิ่มเติมว่า จริงๆ sealand มีหระกรเพิ่มขึ้น 0.000028
เราต้อง update value ของ key "sealand"
วิธีการ update ชื่อตัวแปร[key] = ข้อมูลใหม่
world['sealand'] = 0.000028
#Note python string "" '' ให้ผลลัพท์เหมือนกัน แต่ต้องใช้เป็นคู่

แต่ตอนนี้ อังกฤษไม่ยอมรับ sealand และ กดดันให้สหประชาชาติถอนออกจาก
การเป็นประเทศ
เราต้องการลบ sealand key ออกไปจาก world
ใช้ function del(ตัวแปร[keyที่ต้องการลบ])
del(world['sealand'])
สั่งลบ ตัวแปร Dictionary world
ที่ element ที่ key คือ sealand

ใบงานที่ 2
europe = {"spain":"madrid",
          "france":"paris",
          "germany":"berlin",
          "norway":"oslo",
          "austria":"vienna",
          "belarus":"minsk"}

ต้องการดึงข้อมูลว่า key ของ Dictionary มีอะไรบ้าง
เราจะเรียก method .key() ของตัวแปร dict
europe.keys()
Out[24]: dict_keys(['spain',
                    'france',
                    'germany',
                    'norway',
                    'austria',
                    'belarus']

ใบงานที่ 3
เมืองหลวงของ norway สั่งอย่างไร ได้ผลลัพท์อะไรออกมา 
europe['norway']
Out[33]: 'oslo

เมืองหลวงของ austrlia สั่งอย่างไร ได้ผลลัพท์อะไรออกมา
europe['austrlia']
KeyError: 'austrlia'
เพราะ ไม่มี key austrlia ใน europe


ใบงานที่ 4
europe['italy'] = "rome"
europe['poland'] = "warsaw"

ใบงานที่ 6
เราจะสร้าง Dictionary ซ้อน Dictionary
เป็น ข้อมูลประเทศในยุโรป
ซึ่งแต่ละประเทศ ประกอบด้วยชื่อ name ชื่อเมืองหลวง captial
จำนวนประชากร population
โดยที่เราจะใช้ ชื่อประเทศเป็น key
และให้ value เป็น dict ชั้นที่ 2 ที่เป็น ชื่อเมืองหลวง และ จำำนวนประชากร

europe= { 'spain': { 'capital':'madrid',
                    'population':46.77 },
          'france': { 'capital':'paris',
                     'population':66.03 },  
          'germany': { 'capital':'berlin',
                      'population':80.62},
          'norway': { 'capital':'oslo',
                     'population':5.084 } ,
          'austria': { 'capital':'vienna',
                      'population':3.014 } ,
          'belarus': { 'capital':'minsk',
          'population':8.062 } ,}



ถ้าเอยากเข้าถึงเมืองหลวงของประเทศ france
europe['france']
Out[2]: {'capital': 'paris', 'population': 66.03}
europe['france']['capital']
Out[3]: 'paris'

อยากเข้าถึง จำนวนประชากรของประเทศ belarus สั่งอย่างไร
europe['belarus']['population']
Out[4]: 8.062

ในกรณีที่ europe เป็น dict ซ้อน dict
ถ้าอยากเพิ่ม insert key กับ value ใหม่เข้าไป ก็ใช้แนวคิดเดิม
ชื่อตัวแปร[key อันใหม่] = value อันใหม่
แต่ value เป็น Dictionary
data = {'captial':"rome",'population':59.83}
europe['italy'] = data


ใบงานที่ 7
europe['spain']['population']
Out[9]: 46.77
europe['france']['population']
Out[10]: 66.03
europe['germany']['population']
Out[11]: 80.62
europe['norway']['population']
Out[12]: 5.084
europe['austria']['population']
Out[13]: 3.014
europe['belarus']['population']
Out[14]: 8.062

euro_list = [europe['spain']['population'],
             europe['france']['population'],
             europe['germany']['population'],
             europe['norway']['population'],
             europe['austria']['population'],
             europe['belarus']['population']]

ได้ ตัวเลข 7 ประเทศแล้ว คำนวนค่าเฉลี่ยได้ไหม
mean(euro_list)
NameError: name 'mean' is not defined
mean ไม่ได้เป็น function สถิติ ที่ pythod มาคำนวน
import numpy as np
np.mean(euro_list)
Out[32]: 34.93000000000001

cotrol flow looping ของ pythod
eu_list = []
for k in europe.keys():
    eu_list.append(europe[k]['population'])
import numpy as np
np.mean(eu_list)
Out[23]: 38.487142857142864