'''
You can download the dataset from https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset?resource=download
'''


import pandas as pd 

fake_csv = pd.read_csv('/home/hmicro/Downloads/archive/Fake.csv')
true_csv = pd.read_csv('/home/hmicro/Downloads/archive/True.csv')