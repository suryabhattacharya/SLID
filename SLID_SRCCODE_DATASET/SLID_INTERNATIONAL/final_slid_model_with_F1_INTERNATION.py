#!/usr/bin/env python
# coding: utf-8

# Author:Surya


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import re
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
import xgboost as xgb
import warnings
import os
warnings.filterwarnings('ignore')
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD

path = r'C:\Users\HP\Documents\My_Project\SLID\Final_DATASET\CSV_DATASET'
files = os.listdir(path)

df = []
for file in files:
    data = pd.read_csv('{path}\\{file}')
    df.append(data)

df = pd.concat(df)
df = df[['Filename','text','language']]
df = df1[(df['language']=='Error')]
df['language'].value_counts()


df.head()

lang_code = {}

for index,lang in enumerate(df['language'].unique()):
    lang_code[lang] = index

code_lang = {}

for index,lang in enumerate(df['language'].unique()):
    code_lang[index] = lang

df['lang'] = df['language'].replace(lang_code)

y = df['lang']

df.head()

cv = TfidfVectorizer()
### Converting the text in count vector
X = cv.fit_transform(df['text']).toarray()
X = pd.DataFrame(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)


model = Sequential()

model.add(Dense(units = 100,activation = 'relu',input_shape = (X_train.shape[1],), kernel_initializer='he_uniform'))

model.add(Dense(units = 100,activation = 'relu'))

model.add(Dense(units = 7,activation = 'softmax'))


opt = SGD(lr=0.01, momentum=0.9)

model.compile(loss= 'categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

y_train = to_categorical(y_train)
model.fit(X_train, y_train, batch_size = 10, epochs= 20,validation_split = 0.1)

y_pred = model.predict_classes(X_test)

y_pred = pd.Series(y_pred).replace(code_lang)
y_test = pd.Series(y_test).replace(code_lang)

def plot_confusion_matrix(y_true,predictions):
    cm = confusion_matrix(y_true,predictions,labels = list(lang_code.keys()))
    fig,ax = plt.subplots(figsize = (20,8))
    sn.heatmap(cm,annot = True, fmt = '.0f', cmap = 'YlGnBu', xticklabels = list(lang_code.keys()),yticklabels = list(lang_code.keys()))
    plt.ylabel('Actual',fontsize=20)
    plt.xlabel('Predicted',fontsize=20)
    print('Accuracy Score : ' + str(accuracy_score(y_test,predictions).round(2)))
    return plt.show(block = False)

y_test.value_counts()

plot_confusion_matrix(y_test, y_pred)

#F1 Schore

import sklearn
print(sklearn.metrics.classification_report(y_test, y_pred))


# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr
r = sr.Recognizer()

val = input("Do you want to start the process? If Y, then Say Somthing... (y/n)")

while val == 'y':

    with sr.Microphone() as source:
    
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            text = [text]
            x_1 = cv.transform(text).toarray()
            x_1 = pd.DataFrame(x_1)
            y_1 = model.predict_classes(x_1)
            print(y_1)
            y1_pred = pd.Series(y_1).replace(code_lang)
            print(y1_pred)
            val = input("Do you want to again start the process? If Y, then Say Somthing... (y/n)")
        except:
            print("Sorry could not recognize what you said...")
            val = input("Do you want to again start the process? If Y, then Say Somthing... (y/n)")
            
print('Thank you!!... :)')

"""text = ['text']
#Data = {'Value': [text]}
#df1 = pd.DataFrame(Data) 
x_1 = cv.transform(text)
#x_1 = pd.DataFrame(x_1)
y_1 = model.predict_classes(x_1)
print(y_1)

#y_1 = model.predict(x_1)
#y_1 = y_1.replace(code_lang)
y1_pred = pd.Series(y_1).replace(code_lang)
print(y1_pred)
#print(y_1)"""