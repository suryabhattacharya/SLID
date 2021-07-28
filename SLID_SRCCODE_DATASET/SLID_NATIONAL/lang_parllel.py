"""
Created on Sun Jan 24 15:19:23 2021

@author: surya
"""

import speech_recognition as sr
import os
import pandas as pd
from tqdm import tqdm
import multiprocessing as mp

path = r'C:\Users\HP\Documents\My_Project\SLID\Final_DATASET\iiit_tel_baji\wav'

def text(filename):
    
    try:
        r = sr.Recognizer()
        with sr.AudioFile('{path}\\{filename}') as source:
        # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            print(text)
    #         telgu.append(text)
            data = pd.DataFrame({'Filename':[filename],'text':text})
            data['language'] = 'telgu'
            return(data)
    except:
        data = pd.DataFrame({'Filename':['Error'],'text':'Error'})
        data['language'] = 'Error'
        return(data)
        
    
if _name_== '_main_':
   
    path = r'C:\Users\HP\Documents\My_Project\SLID\Final_DATASET\iiit_tel_baji\wav'
    filenames = os.listdir(f'{path}')    
    pool = mp.Pool(mp.cpu_count())`
    results = tqdm(pool.map(text,filenames))
    pool.close()
    
    results_df = pd.concat(results)
    results_df.to_csv(r'C:\Users\HP\Documents\My_Project\SLID\Final_DATASET\CSV_DATASET\telgu.csv')
    