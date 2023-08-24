
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import pandas as pd
from pycaret.classification import *


def input_preprocessing(data):
   gender = {'Male' : 1, 'Female' : 0}
   
   
   for category,value in gender.items():
    if (data['gender'] == category).all():
      data['gender'] = data['gender'].map(gender)
      data.loc[0, 'gender'] = value
      break
    
    ethinicy = {'group A' : 0, 'group B' : 1, 'group C' : 2, 'group D' : 3, 'group E' : 4}
    
    for category, value in ethinicy.items():
      if(data['race/ethnicity'] == category).all():
        data['race/ethnicity'] = data['race/ethnicity'].map(ethinicy)
        data.loc[0,'race/ethnicity'] = value
        break
    
    parental_education = {"bachelor's degree" :1 , "some college" : 4, "master's degree" : 3, "associate's degree" : 0, "high school" : 2, "some high school" : 5}
    
    for category, value in parental_education.items():
      if(data['parental level of education'] == category).all():
        data['parental level of education'] = data['parental level of education'].map(parental_education)
        data.loc[0,'parental level of education'] = value
        break
      
    lunch = {'standard' : 1, 'free/reduced' : 0}

    for category, value in lunch.items():
      if(data['lunch'] == category).all():
        data['lunch'] = data['lunch'].map(lunch)
        data.loc[0,'lunch'] = value
        break
      
    preparation_test = {'none' : 1, 'completed': 0}

    for category, value in preparation_test.items():
      if(data['test preparation course'] == category).all():
        data['test preparation course'] = data['test preparation course'].map(preparation_test)
        data.loc[0,'test preparation course'] = value
        break
    
    
    min= 0
    max = 100
    min_total = 27
    max_total = 300
    
    data['math score'] = (data['math score'] - min) / ( max - min)
    data['reading score'] = (data['reading score'] - min) / (max - min)
    data['writing score'] = (data['writing score'] - min) / (max- min) 
    data['total score'] = (data['total score'] - min_total) / (max_total- min_total) 

    return data
   
def prediction(gender, ethinicity, parental_education, lunch, test_preparation, math_score,writing_score, reading_score):
  data = pd.DataFrame({
      'gender'                      : [gender],
      'race/ethnicity'              : [ethinicity],
      'parental level of education' : [parental_education],
      'lunch'                       : [lunch],
      'test preparation course'     : [test_preparation],
      'math score'                  : [math_score],
      'reading score'               : [reading_score],
      'writing score'               : [writing_score]

  })
  data['total score'] = data['math score'] + data['reading score'] + data['writing score']

  data = input_preprocessing(data)

  #predict data
  model = load_model('Model/fix_best_model')
  prediction = predict_model(model, data)
  result = prediction.loc[0,'prediction_label']
  prediction_score = prediction.loc[0,'prediction_score']


  return result, prediction_score
  