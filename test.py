import pandas as pd
data_file = "static/data.xlsx"

data = pd.read_excel(data_file ,sheet_name= 'login')
list_user = data.keys().tolist()
print(list_user)
print(data['admin'][0])