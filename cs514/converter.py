import pandas as pd
data = pd.read_stata('Data_1/finlit.dta')
data.to_csv('output2.csv')