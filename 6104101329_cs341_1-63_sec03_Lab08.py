# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:44:53 2020
@author: Nutthawut Promboon6104101329 cs341 sec03
Python Lab8
"""

import pandas as pd

from sklearn import tree

# read ข้อมูลจาก sport_data.csv มาเก็บในตัวแปรชื่อ
# sport_df

sport_df = pd.read_csv("sport_data.csv", index_col=0)

one_hot_data = pd.get_dummies(sport_df[['Outlook',
                                        'Temperature',
                                        'Humidity',
                                        'Windy']])

print(one_hot_data)
# แปลงข้อมูล categorical data ให้กลายเป็น
# numerical data และ logical data

# เราเตรียม dataset ไว้เสร็จเรียบร้อยแล้ว ขั้นตอนถัดไปจะเป็นการสร้าง
# ML แบบ tree model
# เราเรียกอsub modele ชื่อว่า tree ที่อยู่ใน scikit-learn
from sklearn import tree

# สร้าง tree เปล่าๆ แบบ classfication
clf = tree.DecisionTreeClassifier()

# clf เหมือนเป็น object ต้นแบบ
# เราจะ ป้อน training data ให้ clf แล้ว ก๊อปปี้ไปเป็น
# AI ที่ใช้งานจริง

clf_train = clf.fit(one_hot_data, sport_df['Play'])

# แล้วเราก็เอา clf_train ไปใช้จำแนกการแข่งกีฬา

# ในตอนใช้ง่นจริง สโมสรนักศึกษา ถามไปที่กรมอุตุนิยมว่า วันที่จะแข่งขันมีสภาพอากาศอย่างไร
# Test model prediction input:
# Outlook = sunny,
# Temperature = hot,
# Humidity = normal,
# Windy = false
# ข้อมูลที่ได้มาเป็น categorical แต่ AI clf_train อ่านข้อมูล
# ในรูปแบบ one hot data
# เราต้องแปลงวันที่อยากรู้ (unlabeled) ให้อยู่ในรูป one hot data

unlabel = [False, 0, 0, 1, 0, 1, 0, 0, 1]

# เราก็จะจำแนกข้อมูล unlabel ด้วย method .predict
clf_train.predict([unlabel])
# Out[19]: [False, 0, 0, 1, 0, 1, 0, 0, 1]
# มีข้อกำหนดว่า ข้อมูลป้อนเข้า method predict ต้องเป็น array
# หรือ matrix เลยต้องเอา [] ไปครอบข้อมูล

# วันที่เราจะจัดแข่ง unlabel ตัว AI Tree พยากรณ์ว่า yes
# ก็คือ เหมาะกับการแข่งกีฬา


# วันที่ สโมสรกีฬา นักศึกษาเล็งจะแข่งกีฬา มีสภาพอาดาศดังต่อไปนี้
# Test model prediction input:
# Outlook = overcast,
# Temperature = mild,
# Humidity = high,
# Windy = Ture

# Test model prediction input:
# Outlook = rainy,
# Temperature = cool,
# Humidity = normal,
# Windy = Ture
# สร้าง list ของวันทั้ง2 วันมาเป็นข้อมูลป้อนเข้าเพื่อใช้ AI จำแนก
unlabel1 = [True, 1, 0, 0, 0, 0, 1, 1, 0]
unlabel2 = [True, 0, 1, 0, 1, 0, 0, 0, 1]

# classify ข้อมูล unlabel ทั้ง 2 ตัว ด้วย clf_train
clf_train.predict([unlabel1, unlabel2])
# Out[23]: array(['yes', 'no'], dtype=object)

from sklearn import tree 
clf = tree.DecisionTreeClassifier()
clf_train = clf.fit(one_hot_data, sport_df['Play'])

clf_train.predict([unlabel1, unlabel2])

# print tree ออกมาเป็น text based อ่่าน tree ได้ยาก
print(tree.export_graphviz(clf_train, None))

# เราหาทาง print tree เป็น graphic
#Create Dot Data
dot_data= tree.export_graphviz(clf_train, out_file= None,
                               feature_names=list(one_hot_data.columns.values),
                               class_names=['Not_Play', 'Play'], rounded=True,
                               filled=True) 
# เราได้ dot_data มาซึ่งข้างในก็เป็น tree แบบ text based
# แต่เราต้องลง library เพิ่มอีก 1 ตัว เพื่อแสดงในกราฟ ของ tree
# ไม่เกี่ยวกับการสร้าง AI
# เป็นส่วนของการวาด

#########################################################

import pydotplus
from IPython.display import Image
# เอาcode หน้า13 มาวาง
# Create Graph from DOT data
# ที่บรรทัดนี้อาจมีบางคนเกิดerrorที่ lib graphviz
# เป็นปัญหาที่ lib กับ การ์ดจอ
graph = pydotplus.graph_from_dot_data(dot_data)

Image(graph.create_png())































