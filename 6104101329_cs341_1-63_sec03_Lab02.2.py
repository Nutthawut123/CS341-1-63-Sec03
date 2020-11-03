# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:09:32 2020
@author: Nutthawut Promboon6104101329
Introduction to Python Lab2
"""

#คาบที่3
เราสร้าง list ซ้อน list
x_list = [["a","b","c"],["d","e","f"],["g","h","i"]]
x_list[0]
Out[5]: ['a', 'b', 'c']
x_list[2]
Out[6]: ['g', 'h', 'i']
x_list[0][0]
Out[8]: 'a'
จะเห็นว่าคล้ายกับการเข้าถึง array 2 มิติของ C
selsct หลายๆ element ได้
x_list[0][1:2]
Out[9]: ['b']
x_list[0][1: ]
Out[10]: ['b', 'c']
x_list[0][1:3]
Out[11]: ['b', 'c']
x_list[0][1:4]
Out[12]: ['b', 'c']
แล้วถ้าอยากได้[b,c][e,f]
x_list[0:2][1: ]
Out[13]: [['d', 'e', 'f']]
นี้คือข้อจำกัดของ list ในภาษา python
แต่เพื่อ support งานแบบนี้ ต่อไปเราเรียก DS ที่ช่วยทำได้
เราเรียกว่า package numpy

fam = ["liz",1.73, "emma",1.68, "mom",1.17, "dad",1.89]
fam[7]
Out[15]: 1.89
#changing value in element
fam[7] = 1.86
#changing value in multi element
fam[0:2] = ["liza",1.74]
#adding element by +
fam_ext = fam + ["me",1.79]
#delete element by del
del(fam_ext[8])
#อยากลบ me
del(fam_ext[8])
#คำเตือน การลบ element ของ list
#จะหายไปจาก memory ถาวร

x_ch = ["a","b","c"]
y_ch = x_ch #ประกาศแบบนี้ใช้พท.mem เดียวกัน
y_ch[1] = "z"
y_ch = x_ch[ : ]
#select ทั้งหมดใน x_ch ไปไว้ที่ y_ch
y_ch[1] = "b"
#สร้างพท. mem ใหม่ แล้วก๊อปปี้ ของใน x_ch ไปไว้ใน y_ch
y_ch = list(x_ch)


areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
areas[9] = 10.50
areas[4] = "chill zone"

areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0, "bedroom", 10.75, "bathroom", 10.50]
areas_1 = areas + ["poolhouse", 24.5] 
areas_2 = areas_1 + ["garage",15.45]
