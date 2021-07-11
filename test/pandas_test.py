import pandas as pd

DEBUG_CSV_PATH = "/Users/yakozen/PycharmProjects/test/csv/MOCK_DATA.csv"
df = pd.read_csv(DEBUG_CSV_PATH, sep=',')

child_list = df['child'].unique()
parent_list = df['parent'].unique()

print(parent_list)
print(child_list)
