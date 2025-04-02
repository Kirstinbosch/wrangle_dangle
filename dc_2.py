import pandas as pd
df = pd.read_excel(r"/Users/kirstincathlin/PycharmProjects/data_cleaning.py/Customer Call List.xlsx")

df = df.drop_duplicates()
df = df.drop(columns = 'Not_Useful_Column')

#df["Last_Name"] = df["Last_Name"].astype(str).str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].astype(str).str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].astype(str).str.rstrip("_")
df["First_Name"] = df["First_Name"].astype(str).str.rstrip()
df["Last_Name"] = df["Last_Name"].astype(str).str.strip("123._/")

df["Phone_Number"] = df["Phone_Number"].astype(str).str.replace(r'[^a-zA-Z0-9]','', regex = True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
print(df.iloc[:,4])
#df["Address"] = df["Address"].str.split(',',2, expand=True)
#print(df.iloc[:,0:5])
