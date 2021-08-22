import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score 
from sklearn.utils import shuffle

'''
  NOTES:
  B - harmless
  M - cancerous
'''

# FEATURE SELECTION
def remove_correlated_features(X):
  pass

def remove_features(X, Y):
  pass

# MODEL TRAINING
def compute_cost(W, X, Y):
  pass

def calculate_cost_gradient(W, X_batch, Y_batch):
  pass

def sgd(features, outputs):
  pass

def init():
  data = pd.read_csv('./data.csv')

  # CONVERT TO NUMERICAL VALUES
  diagnosis_map = {'M' : 1, 'B' : -1}
  data['diagnosis'] = data['diagnosis'].map(diagnosis_map)
  
  print(data)

init()