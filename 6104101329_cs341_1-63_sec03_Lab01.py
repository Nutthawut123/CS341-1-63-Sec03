# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:26:28 2020

@author: Nutthawut Promboon6104101329
Introduction to Python Lab1

"""

# คาบที่ 1
#ใบงานที่ 1
100 * 1.1
110.00000000000001

100 * 1.1* 1.1* 1.1* 1.1* 1.1* 1.1* 1.1
194.87171000000015

100 * 1.1 **7
194.87171000000012

#bmi = weight / height * height
#ผิด
#bmi = weight / ( height * height )
#bmi = weight / height **2
21.44127836209856

#print(bmi)
21.44127836209856

#type (bmi)
#Out[17]: float

day_of_week = 5
int
day_of_week = 5.0
float
day_of_week = "Sunday"
str
day_of_week = True
bool
day_of_week = "False"
str

#'abc'+'abc'
#'abcabc'

#ใบงานที่ 2
100*1.1**10
259.3742460100002

savings = 100
factor = 1.1
result = savings * factor **10

#ใบงานที่ 3
desc = "compound interest"
Boolean = True

type(desc)
Out[7]: str
type(Boolean)
Out[8]: bool

res = "is result of calcuotion"
desc+res
#Out[7]: 'compound interestis result of calcuotion'
#operation sum (+) สำหรับ string คือการตอบข้อความ

type(desc)
Out[8]: str

result = 150
type(result)
Out[12]: int

desc+result
#ได้ error เพราะคนละชนิดข้อมูลกัน
#คือมีการแปลงข้อมูลก่อน
#ถ้าต้องการแปลงข้อมูลใดๆ ให้เป็น string str()

desc + str(result)
#Out[17]: 'compound interest150'

#ใบงานที่5
savings = 100
result - savings * 1.1**7
Out[19]: -44.87171000000012

print("I strated with $" + str(savings) + "and now have %" + str(result) + ". Awesome!")

#output I strated with $100and now have %150. Awesome!

True+False
Out[25]: 1

# False = 0
# True = 1













