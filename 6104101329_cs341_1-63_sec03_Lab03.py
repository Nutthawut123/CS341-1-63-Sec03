# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:38:32 2020
@author: Nutthawut Promboon6104101329
Introduction to Python Lab3
"""
fam_num = [1.73, 1.68, 1.71, 1.89]
ถ้าเราอยากทราบว่าตัวเลขที่สูงที่สุดคือตัวเลขใด
ในอดีต ภาษา C เราต้องเขียนคำสั่งวนรอบหาค่าสูงสุด
ในปัจจุบันภาษาสมัยใหม่ได้เตรียม function ไว้ให้แล้ว
function max()

max(fam_num)
Out[40]: 1.89

นั้นคือเราเรียก call function max
พร้อมกับ ป้อนข้อมูลให้คือ fam_num
แล้วรให้ max ตอบผลลัะธ์ ออกมาเป็นตัวเลข
ข้อมูลที่ป้อนเข้า เรียกว่า input
ข้อมูลผลลัพธ์ที่ได้จาก function เรียกว่า output

talleat = max(fam_num)
ประกาศตัวแปร talleat แล้ว
assign ค่าด้วยการ call function max()
แล้ว input ด้วย fam_num

1.68 #floating point
ทศนิยม 2 ตำแหน่ง หลัง . จุดทศนิยม 2 หลัก
decimal 2 digits
ถ้าเราต้องการป้อนเลขทศนิยมไปเป็นเลขจำนวนเต็ม integerdeci
round(1.68)
Out[42]: 2 #คือตัวเลขที่ได้จากการป้อนเลขทศนิยม 1.68
round(1.68,1)
Out[43]: 1.7 #ปัดตัวเลขจากสองตำแหน่งเหลือ1ตำแหน่ง
#แสดงว่า input ตัวที่ 2 สามารถกำหนด
#ตำแหน่งทศนิยมที่ต้องการปัดได้
round(1.68,0)
Out[44]: 2.0
#แตกต่างกับ
round(1.68)
Out[45]: 2
#เราจะเห็นได้ว่ารูปแบบการป้อน input มีหลากหลาย
#แล้วเราจะรู้ได้ไงว่า ป้อนแบบนี้
help(round)
round(number, ndigits=None)
function round()
input ประกอบด้วย 2 อัน
number คือตัวเลขที่เราจะปิดค่า
ndigts คือหลักทศนิยมที่เราอยากได้เป็นผลลัพธ์
ให้สังเกตุว่า ndigts มีการใส่ = None กำกับไว้
แปลว่า ตอน call round ไม่ใส่ ndigts ก็ได้
โปรแกรมจะถือว่าเป็น None (set default)
round(1.68)
Out[48]: 2
round(1.68, ndigits=None)
Out[49]: 2
round(1.68, None) #ปัดเป็นเลขจำนวนเต็ม
Out[52]: 2
round(None,1.68) #ลำดับ input ผิด
#error
#input ของ function เราเรียก argument

sister = "liz"
sister เป็น string objest
type(sister)
Out[55]: str
เรียกใช้ function ที่เกี่ยวข้องกับ string
len(sister)
Out[56]: 3 #หาความยาวของ sister
เรียกใช้ methon ที่ติดมากับ string
sister.capitalize()
Out[57]: 'Liz' #เปลี่ยนอักขระตัวแรกเป็น L
#ให้สังเกตุความแตกต่างระหว่างการเรียกใช้ call
function กับ methon 
len เป็น function เรียกใช้ได้โดยตรง
capitalize เป็น methon เรียกผ่าน string object

type(fam)
Out[58]: list
fam_num.index(1.73)
Out[59]: 0
fam_num.index(1.71)
Out[60]: 2
เรียกใช้ methon index ผ่าน obj fam_num โดยป้อน 
ตัวเลข1.71 เข้าไป
fam_num.index(1.89)
Out[61]: 3
fam_num.index(1.45)
#ValueError: 1.45 is not in list
index.fam_num(1.89)
#NameError: name 'index' is not defined
#แปลว่าไม่มี function index

คนละ obj แต่ก็อาจจะมี methon ที่ชื่อคล้ายกันและทำงานคล้ายกัน
sister
sister.index("z")
Out[64]: 2

""""""""""""""""""""""""""""""""""""

method ที่มากับตัวแปร obj string
sister.replace("z", "sa")
Out[1]: 'lisa'
#จะเห็นว่า ข้อมูลใน workspacew ยังเป็น "liz"
#แต่การแสดงผลลัพธ์ของ method replace "lisa"

#ลองสังเกตุ method ของ obj อื่นๆบ้าง
#obj list
type(fam)
Out[2]: list
fam.append("me")
#append คือ method ของ list ที่นำข้อมูล input มาต่อท้าย list ที่เรียก method
#สังเกตุว่าผลลัพธ์ต่อท้ายไม่ได้แสดงออกทาง console แต่มันเป็นการอัพเดตข้อมูลที่อยู่ใน fam ให้กลายมามี 9 element

#ถ้าไม่อยากอยู่กับข้อมูล original เราใช้วิธีเรียก method แล้ว assign ผลลัพธ์ไปยังตัวแปร

fam
Out[7]: ['liza', 1.74, 'emma', 1.68, 'mom', 1.17, 'dad', 1.86]
fam.append("me")
fam
Out[9]: ['liza', 1.74, 'emma', 1.68, 'mom', 1.17, 'dad', 1.86, 'me']

fam_ext = fam[:]
fam_ext
Out[11]: ['liza', 1.74, 'emma', 1.68, 'mom', 1.17, 'dad', 1.86, 'me']
fam_ext.append(1.68)
fam_ext
Out[13]: ['liza', 1.74, 'emma', 1.68, 'mom', 1.17, 'dad', 1.86, 'me', 1.68]

#จะเห็นว่า fam_ext ที่มีข้อมูลเพิ่มเติม จะไม่ไปยุ่งกับ fam ตัวเดิม

ใบงานที่1
first = [11.25,18.0,20.0]
second = [10.75,9.50]
full = first + second 
full
Out[17]: [11.25, 18.0, 20.0, 10.75, 9.5]

#เรามาลองเรียงลำดับข้อมูลใน full ด้วย function sorted()
full_sorted = sorted(full,reverse = True)
full_sorted
Out[24]: [20.0, 18.0, 11.25, 10.75, 9.5]
# True ตัวเลขจากมากไปน้อย ภาษาอังกฤษเรียกว่า Descending DEEC
full_sorted = sorted(full,reverse = False)
full_sorted
Out[26]: [9.5, 10.75, 11.25, 18.0, 20.0]
#ตัวเลขจากน้อยไปมาก ภาษาอังกฤษเรียกว่า Ascending ASC

#ถ้า argument reverse ไม่ใส่จะเกิดอะไรขึ้น
full_sorted = sorted(full)
full_sorted
Out[28]: [9.5, 10.75, 11.25, 18.0, 20.0]

#ค่า default ของ reverse เป็น อะไร False

full_sorted = sorted(full,reverse = False)
full_sorted
Out[30]: [9.5, 10.75, 11.25, 18.0, 20.0]

ใบงานที่2
room = "poolhouse"
#แปรงตัวอักษาทุกตัวใน room ให้ไปเป็นตัวอักษรใหญ่
#ด้วยการเรียก methon upper ซึ่งต้องเรียกผ่าน obj string room
#แล้วผลลัพธ์ที่ได้จากการเรียก upper จะนำไปเก็บใน room_up
room_up = room.upper()
print(room) #poolhouse
print(room_up) #POOLHOUSE
#จะเห็นว่า method upper ไม่ได้ไปแก้ไขข้อมูลใน room
#แต่เป็นการแปรงตัวอักษรเป็นตัวใหญ่ขึ้นในคอมพิมพ์ออกหน้าจอ

#มี method มาอันที่ นอกจาก call ผ่าน obj แล้ว
#ยังต้อง ป้อน argument เข้าไปด้วย เหมือน function
room.count("o")
Out[38]: 3
room.count("O")
Out[39]: 0
#จะเห็นว่า method ก็คือ function ที่ติดมากับ object
#จะเรียก method ต้อง เรียกใช้ผ่า object เสมอ

#คำสั่งเรียกใช้ package numpy
import numpy
ModuleNotFoundError:
    No module named 'numpy'
#เจอแบบนี้แปลว่า ยังไม่ได้ install numpy
    
import numpy
#ถ้า run บรรทัดนี้แล้วไม่เกิด error แปลว่า install สำเร็จ
#ตอนนี้เราสามารถเรียกใช้ method ที่อยู่ใน numpy
#method array
array([1,2,3])
NameError: name 'array' is not defined
ตัวแปรภาษายังงอยู่ว่า array method หาไม่พบ

numpy.array([1,2,3])
Out[42]: array([1, 2, 3])

arr1 = numpy.array([1,2,3])
arr1
Out[45]: array([1, 2, 3])
วิธีนี้คือการ import module numpy เข้ามาในโปรแกรม
ต่อจากนั้นเรียก method array เพื่อสร้างข้อมูล array
ที่มีตัวเลข 1 2 3
ใครงสร้างข้อมูล arr1 เรียกว่า numpy array

#วิธีการ import module และ call method มีได้หลายๆแบบ

import numpy as np
#การ import module หรือ package พร้อมทั้ง
#สร้าง instance ของ module นั้นๆ ด้วยคำสั่ง as
#ซึ่งจะได้ np เป็น instance ของ numpy
arr2 = np.array([1,2,3])
arr2
Out[48]: array([1, 2, 3])
#ถ้าประกาศแบบนี้ ต่อไปเราไม่ต้องเรียก numpy เราเรียก np
#ก็สามารถ call method ใน numpy ได้
#np จะไม่เห็นว่าอยู่ใน Variable explorer
#เพราะ np ไม่ใช่ตัวแปร แต่เป็น class instance

#บางครั้งเราก็อยากประกาศ ให้บาง method มีลักษณะเป็น fuction
#อย่างเช่น method array ที่อยู่ใน numpy
from numpy import array
arr3 = array([1,2,3])
arr3
Out[49]: array([1, 2, 3])
#ต่อจากนี้ array mrthod สามารถเรียกใช้ได้ในรูปแบบ function
#โดยไม่ต้อง call ผ่าน object numpy แล้ว
#เพราะเราบอก ตัวแปรภาษาไว้ตอน from numpy แล้ว

#ทำไมต้อง numpy 
height = [1.73,1.68,1.71,1.89,1.79]
weight = [65.4,59.2,63.6,88.4,68.7]
#เราสามารถดูสุขภาพดีหรือไม่ผ่านค่า BMI
#BMI คำนวนจาก น้ำหนัก / ส่วนสูง ยกกำลัง2
weight / height **2
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

error บอกเราว่า วิธีการคำนวนแบบนี้ 
Data structure แบบ list ไม่ support
ข้อจำกัดนี้ ทำให้เกิดการพัฒนา package numpy ขึ้นมานั้นเอง

#สร้าง numpy array np_height
np_height = np.array(height)
np_height
Out[53]: array([1.73, 1.68, 1.71, 1.89, 1.79])
#สร้าง numpy array np_weight
np_weight = np.array(weight)
np_weight
Out[57]: array([65.4, 59.2, 63.6, 88.4, 68.7])

np_weight / np_height**2
Out[58]: array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])
รูปแบบคำสั่งที่ list ทำไม่ได้ numpy สามารถคำนวนได้ 
np_bmi = np_weight / np_height**2
np_bmi
Out[59]: array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])
#จะเห็นได้ว่า numpy array คำนวนกับ numpy array
#จะได้ผลลัพธ์เป็น numpy array เช่นเดียวกัน

#เรื่องสุดท้ายคือข้อควรระวัง การประกาศ numpy arrray ที่ข้อมูล
#ประกอบด้วยหลายๆชนิด
np.array([1.0,"is",True])
Out[60]: array(['1.0', 'is', 'True'], dtype='<U32')
ผลลัพธ์ที่ได้ array จะเป็น string ทั้งหมด
เพราะ nnump array มีเงื่อนไข่า
1 ข้อมูลที่เก็บ ต้องเป็นชนิดเดียวกันเท่านั้น
2 ถ้าเป็นข้อมูลป้อนเข้าตนละชนิด มันจะ cast ไปเป็นชนิดที่ใหญ่ที่สุด
string > floating > integer > logic

"""""""""""""""""""""""""""""""""""""

#การเลือกบางส่วนใน Numpy array Subsetting
np_bmi
Out[1]: array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])

bmi = [21.852, 20.975, 21.750, 24.747 , 21.441]

ก่อนจะเรียกใช้ Numpy package เราต้องมีการ import numpy เข้ามา
import numpy as np
#np เป็น instance ของ object numpy
np_bmi = np.array(bmi)

เปรียบเทียบข้อมูลใน np_bmi ว่า element ไหนมีค่ามากกว่า23
np_bmi
Out[9]: [21.852, 20.975, 21.75, 24.747, 21.441]
np_bmi > 23
Out[19]: array([False, False, False,  True, False])

#การเลือกบางส่วน Subsetting ใช้สัญลักษณ์ [] square bracket
np_bmi[np_bmi > 23]
Out[32]: array([24.747])
#การทำ Subsetting โดยไม่มีเงื่อนไข np_bmi > 23 แล้วมีผลเป็น Ture
#Subsetting by condition เลือกเฉพาะอันที่มีเงื่อนไขเป็น Ture
ถ้า bmi เกิน 23 แปลว่า เริ่มอ้วน
คนที่ผอม คือ คนที่ bmi ต่ำกว่า 21 อยากได้ตัวเลขนั้นสั่งอย่างไร (<)
np_bmi >=21 & np_bmi <=23
ในตอนนี้เรายังไม่รู้วิธีเชื่อม condition เดียวจะได้เรียนต่อไป

คำสั่งดูชนิดของตัวแปร type()
type(np_bmi)
Out[33]: numpy.ndarray
มีความหมายว่า เป็น Attribute ของ numpy object แบบ  array()
ndarray หมายถึง n มิติ (dimension)
n เป็นจำนวนมิติ แปลว่า สามารถสร้างข้อมูลได้หลายๆมิติ
np_bmi 1darray เพราะ มีแค่ 1 มิติ ข้อมูลมีแถวเดียว

ในกรณีที่อยากสร้างมากกว่า1 มิติ เช่น 2d array()
สร้าง array 2 มิติ จากข้อมูล list ซ้อน list
np_2d = np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,68.7]])
In [35]: np_2d = np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,68.7]])

เราอยากทราบรูปทรงของ array เราใช้คำสั่ง shaoe
shape เป็น Attribute ของ np_2d
np_2d.shape
Out[36]: (2, 5)

shape เป็น Attribute ไม่ใช่ methon
np_2d.shape()
TypeError: 'tuple' object is not callable
shape มีไว้บอกขนาดของ มิติทั้ง 2 แกน
แกนแถว Row มี 2 แถว index 0 กับ 1
แกนคอลัมน์ Colmn มี 5 คอลัมน์ index0-4
เราพิจารณา แถว ก่อน คอลัมน์
array 2 มิตินี้ เราเรียกมันว่า Matrix m x n (m แถว n คอลัมน์)

np_2d_str = np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,"59.2",63.6,88.4,68.7]])
In [38]: np_2d_str = np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,"59.2",63.6,88.4,68.7]])
#np_2d_str จะไม่ได้เป็น matrix ของตัวเลข จะเป็น string
#จากกฎที่บอกว่า numpy array ข้อมูลที่อยู่ข้างในต้องเป็น
#single data type

Subsetting 2d array ได้ด้วยวิธีการ indexing
np_2d[0]
Out[39]: array([1.73, 1.68, 1.71, 1.89, 1.79])

np_2d[1]
Out[40]: array([65.4, 59.2, 63.6, 88.4, 68.7])

ในบางกรณีเราเลือกทั้งแนวแถวแนวคอลัมน์
np_2d[0][2] #แถว index0 คอมลัมน์ index2
Out[41]: 1.71

np_2d[0,2] #เป็นรูปแบบอ้างอิง index ของ ptyhon
Out[42]: 1.71

#subseting หลายตำแหน่งต่อเนื่องกัน ได้ด้วย :
np_2d[ :, 1:3] # : เปล่าๆแปลว่าเอาทั้งหมเด
Out[44]: array([[ 1.68,  1.71],[59.2 , 63.6 ]])

np_2d[1, : ]
Out[46]: array([65.4, 59.2, 63.6, 88.4, 68.7])

np_2d[0:1, 1:4]
Out[47]: array([[1.68, 1.71, 1.89]])


เราจะสร้าง matrix ของ เมือง 6 แทือง
เก็บเลขจำนวนประชากร (หลักล้าน) พื้นที่(ตร.กม.)
np_city = np.array([[1.64, 71.78],
                    [1.37, 63.35],
                    [1.6, 55.69],
                    [2.04, 55.09],
                    [2.04, 68.72],
                    [2.01,73.57]])

ได้ matrix ที่มีขนาด 6 x 2
6 แถว แทน เมืองทั้ง 6 เมือง
2 คอลัมน์ แทน ข้อมมูล จำนวนประชากร และ พท. ตามลำดับ

ถ้าอยากรู้ว่า โดยเฉลี่ย 6 เมืองมีประชากรจำนวนเท่าไหร่ เราต้องทำอย่างไร
แต่ภาษา ptyhon ได้เตรียม function methon ในการคำนวน
ค่าทางสถิติไว้ให้แล้ว
ค่าเฉลี่ย mean เป็น method หนึ่งใน np instance
np.mean(np_city[ : ,0])
Out[50]: 1.7833333333333332
เรียกไปที่ instance np แล้วเรียก method mean
แล้วป้อน argument เป็นข้อมูล ที่เลือกมาจาก np_city
เอาทุก แถว : และ เลือกเฉพาะ คอลัมน์ 0 

mean ค่าเฉลี่ย
median ค่ามัธยฐาน
อยากได้ค่ามัธยฐานของพื้นที่เมืองทั้ง 6 เมือง
np.median(np_city[:, -1])
Out[52]: 66.035

np.std() ค่าส่วนเบี่ยงเบนมาตรฐาน
ถ้าอยากปัดตัวเลข round()
np.round(np.mean(np_city[:, 0]),2)
Out[56]: 1.78
เรียก method round ของ np
ป้อนค่าเฉลี่ยที่กำหนดจากการเรียก method mean ของ np
ป้อนค่าจำนวนประชากรโดยการ select ทุกแถว คอลัมน์ 0
แล้วบอก round ว่าปัด 2 ตำแหน่ง

ใบงานที่ 5
height = [74,74,72,72,73,69,69,71]
import numpy as np
np_height = np.array(height)
type(np_height)
Out[60]: numpy.ndarray
np_height = np_height * 0.0254
#np_baseball_m = np.multiply(np_height,0.0254)
np_baseball_m = np.array(np_height)
np_height
Out[63]: array([[1.8796, 1.8796, 1.8288, 1.8288, 1.8542, 1.7526, 1.7526, 1.8034]])
np_baseball_m
Out[64]: array([[1.8796, 1.8796, 1.8288, 1.8288, 1.8542, 1.7526, 1.7526, 1.8034]])

weight = [180,215,210,210,188,176,209,200]
np_weight = np.array(weight)
np_weight_kg = np_weight * 0.453592

bmi = np_weight_kg/np_baseball_m**2
bmi
Out[73]: 
array([[23.11037639, 27.60406069, 28.48080465, 28.48080465, 24.80333518,
        25.99036864, 30.86356276, 27.89402921]])

ใบงานที่ 6
bmi < 24
Out[74]: array([[ True, False, False, False, False, False, False, False]])

bmi[bmi<24]
Out[75]: array([23.11037639])

ใบงานที่ 7 
baseball = [[180,78.4],
            [215,102.7],
            [210,98.5],
            [188,75.2],
            [183,73]]

แปลง list baseballball ไปเป็น ni=umpy array np_baseball
np_baseball = np.array(baseball)
ใช้คำสั่ง หาขนาด shape ของ np_baseball
np_baseball.shape
Out[82]: (5, 2)

ใบงานที่ 10
อยากทราบ ค่าเฉลี่ยความสูงของนักกีฬาทั้ง 5 คน (ความสูงเป็น คอลัมน์ index 0)
np.mean(np_baseball[ : ])
Out[85]: 140.38
อยากทราบ มัธยฐานของน้ำหนักของรักกีฬาทั้ง 5 คน (น้ำหนัก คอลัมน์ index 1 )
np.median(np_baseball[ : ])
Out[84]: 141.35
อยากดึงข้อมูล ทั้งความสูงและน้ำหนักของนักกีฬาคนที่ 2 และ3 ออกมา
bassball[1:3]
Out[97]: [[215, 102.7], [210, 98.5]]





