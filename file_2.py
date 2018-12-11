import pandas as pd
import numpy as np

def change(i):
	print(i)
	i = "{num:>02}".format(num="i")
	return i ;

data = pd.io.stata.read_stata('C:/CU Sem 1/RuthProject/transaction_food_items_monthly.dta')
data.to_csv('C:/CU Sem 1/RuthProject/my_stata_file.csv')

df = pd.read_csv('C:/CU Sem 1/RuthProject/my_stata_file.csv')
df2 = pd.read_csv('C:/CU Sem 1/RuthProject/mymap.csv')

df1 = df[df['item_unit']!='rs']

c=df1.merge(df2,on="item_name")

c.to_csv('C:/CU Sem 1/RuthProject/new_file_oth.csv')


df = pd.read_csv('C:/CU Sem 1/RuthProject/new_file_pur.csv')
df1 = pd.read_csv('C:/CU Sem 1/RuthProject/new_file3.csv')
df1.columns=['vds_id','contrib']
df.groupby('survey_year').sum()
c=df.merge(df1,on="vds_id");


# print("{:02}".format(1));

# df.survey_month.apply(str);
# h={1:"Jan",2:"Feb",3:"Mar"};


df.loc[df.survey_month <= 9, 'new_Col'] = df.survey_month.astype(str).str.zfill(2)
df.loc[df.survey_month > 9, 'new_Col'] = df.survey_month 
print(df.new_Col)


df.survey_month=df.survey_month.apply(lambda x: "%02d" % x)

df['date'] = df['survey_month']++"/"df['survey_year'].map(str)

# #df['survey_month']+=int("0"+chr(df['survey_month']));


df['tot_cal']=df.tot_cal*df.qty_pur
df['tot_iron']=df.tot_iron*df.qty_pur
df['tot_zinc']=df.tot_zinc*df.qty_pur
df['tot_protein']=df.tot_protein*df.qty_pur

df.to_csv('C:/CU Sem 1/RuthProject/new_file_pur.csv')