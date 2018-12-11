import pandas as pd
df = pd.read_csv('C:/CU Sem 1/RuthProject/plot2.csv')
df = pd.read_csv('C:/CU Sem 1/RuthProject/final_oth1.csv')
df1 = pd.read_csv('C:/CU Sem 1/RuthProject/pur_data_final1.csv')

df.columns=['vds_id','year','contrib']

print("merged")

df1.set_index(['vds_id','year'])
df.set_index(['vds_id','year'])



df=df.merge(df1,how='left',on=['vds_id','year'])
df=df.fillna(method='ffill')
print(df)
df.to_csv('C:/CU Sem 1/RuthProject/plot.csv');


df['tot_cal_pur'] = 0
for index,rows in df.iterrows():
	df.loc[index,'tot_cal_n'] = rows['tot_cal_pur']/df1.loc[index]['contrib']

print(df.head(2))
df = pd.read_csv('C:/CU Sem 1/RuthProject/plot.csv')
df['tot_cal']=df['tot_cal']/df['contrib']
df['tot_protein']=df['tot_protein']/df['contrib']
df['tot_zinc']=df['tot_zinc']/df['contrib']
df['tot_iron']=df['tot_iron']/df['contrib']


df.to_csv('C:/CU Sem 1/RuthProject/plot2.csv');