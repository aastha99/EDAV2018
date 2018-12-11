import pandas as pd
import numpy as np

df = pd.read_csv('C:/CU Sem 1/RuthProject/my_stata_file.csv')
df2 = pd.read_csv('C:/CU Sem 1/RuthProject/mymap.csv')

# df=df.iloc[:,1:11]

df1 = df[df['item_unit']!='rs']

c=df1.merge(df2,on="item_name")

c.to_csv('C:/CU Sem 1/RuthProject/final_pur.csv')

df = pd.read_csv('C:/CU Sem 1/RuthProject/final_pur.csv')
df.survey_month.apply(str);

df1 = pd.read_csv('C:/CU Sem 1/RuthProject/new_file_oth.csv')

df.survey_month=df.survey_month.apply(lambda x: "%02d" % x)
print(df.survey_month)
df['date'] = df['survey_month']+"/"+df['survey_year'].map(str)
print(df['date'])
df.to_csv('C:/CU Sem 1/RuthProject/final_pur.csv')
df['tot_cal']=df.tot_cal*df.qty_pur
df['tot_iron']=df.tot_iron*df.qty_pur
df['tot_zinc']=df.tot_zinc*df.qty_pur
df['tot_protein']=df.tot_protein*df.qty_pur


df1['tot_cal']=df.tot_cal*df.qty_ot
df1['tot_iron']=df.tot_iron*df.qty_ot
df1['tot_zinc']=df.tot_zinc*df.qty_ot
df1['tot_protein']=df.tot_protein*df.qty_ot

df.to_csv('C:/CU Sem 1/RuthProject/final_pur.csv')

df1.to_csv('C:/CU Sem 1/RuthProject/new_file_oth1.csv')
