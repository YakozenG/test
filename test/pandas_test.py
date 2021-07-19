import pandas as pd

DEBUG_CSV_PATH = r'/Users/yakozen/Documents/GitHub/test/test/csv/MOCK_DATA.csv'
CULUMN_LIST = ['id', 'Maker', 'Year', 'PartNumber', 'Material']
df = pd.read_csv(DEBUG_CSV_PATH, sep=',')

child_list = df['Material'].unique()
parent_list = df['PartNumber'].unique()


print(parent_list)
print(child_list)
