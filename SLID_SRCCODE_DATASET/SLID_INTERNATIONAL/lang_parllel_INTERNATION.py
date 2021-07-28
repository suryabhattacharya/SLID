"""
Created on Sun Jan 24 15:19:23 2021

@author: surya
"""

import speech_recognition as sr
import os
import pandas as pd
from tqdm import tqdm
import multiprocessing as mp

path = r'C:\Users\HP\Documents\My_Project\SLID\TEST_INTERNATIONAL_DATASET\New_Dataset_6_Lang\Bangla'

def text(filename):
    
    try:
        r = sr.Recognizer()
        with sr.AudioFile(f'{path}\\{filename}') as source:
        # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            print(text)
            # telgu.append(text)
            data = pd.DataFrame({'Filename':[filename],'text':text})
            data['language'] = 'telgu'
            return(data)
    except:
        data = pd.DataFrame({'Filename':['Error'],'text':'Error'})
        data['language'] = 'Error'
        return(data)
        
    
if _name_ == '_main_':
   
    path = r'C:\Users\HP\Documents\My_Project\SLID\TEST_INTERNATIONAL_DATASET\New_Dataset_6_Lang\Bangla'
    filenames = os.listdir(f'{path}')

    
    pool = mp.Pool(mp.cpu_count())
    results = tqdm(pool.map(text,filenames))
    pool.close()
    
    results_df = pd.concat(results)
    results_df.to_csv(r'C:\Users\HP\Documents\My_Project\SLID\TEST_INTERNATIONAL_DATASET\New_Dataset_6_Lang\INTERNATIO_CSV_DATASET\bangla.csv')
    