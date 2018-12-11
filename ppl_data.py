import pandas as pd
import numpy as np

df = pd.read_csv('C:/CU Sem 1/RuthProject/Dataset/A.Household_details_2011.csv',error_bad_lines=False,lineterminator='\n');

dfa = pd.read_csv('C:/CU Sem 1/RuthProject/Dataset/A.Household_details_2010.csv',error_bad_lines=False,lineterminator='\n');
dfb = pd.read_csv('C:/CU Sem 1/RuthProject/Dataset/A.Household_details_2012.csv',error_bad_lines=False,lineterminator='\n');
dfc = pd.read_csv('C:/CU Sem 1/RuthProject/Dataset/A.Household_details_2013.csv',error_bad_lines=False,lineterminator='\n');
dfd = pd.read_csv('C:/CU Sem 1/RuthProject/Dataset/A.Household_details_2014.csv',error_bad_lines=False,lineterminator='\n');
df1 = pd.DataFrame(data=df);
data = df1.groupby(by=['VDS_ID']);

df['Total']=pd.Series(df['VDS_ID'].sum(), index = ['VDS_ID'])
def check_val(a,b):
	if a=="nan":
		return 0,0
	elif a=="Male" and b>18:
		return 1.2,2
	elif a=="Female" and b>18:
		return 0.9,1
	elif b<4:
		return 0.4,0
	elif b<8:
		return 0.5,0
	elif b<12:
		return 0.8,0
	else:
		return 1,0



#df.drop_na(how:"all");
#df.append([dfa,dfb,dfc,dfd])

frames = [df,dfa,dfb,dfc,dfd]
# df1=pd.concat(frames,ignore_index=True)
# frames1 = [df1,dfb]
# df2=pd.concat(frames1,ignore_index=True)
# frames2 = [df,dfc]
# df=pd.concat(frames2,ignore_index=True)
# frames3 = [df,dfd]
dfx=pd.concat(frames,ignore_index=True).drop_duplicates();
print(dfx.columns)
dfx=dfx[['VDS_ID','YEAR','GENDER','AGE']]
dfx.to_csv('C:/CU Sem 1/RuthProject/merged_household_old.csv')



dfx['contrib']=0
dfx['gender_new']=0
#print(df.columns)

for index,row in dfx.iterrows():
	inp_data = check_val(row['GENDER'],row['AGE'])
	print(inp_data[0])
	dfx.loc[index,'contrib']=inp_data[0]
	dfx.loc[index,'gender_new']=inp_data[1]

	#print(row['contrib'])
print(len(dfx))

dfx = dfx.groupby(['VDS_ID','YEAR'])['contrib'].sum();


#print(df.columns)

dfx.to_csv('C:/CU Sem 1/RuthProject/merged_household.csv')