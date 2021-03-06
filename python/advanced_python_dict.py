import re
import pandas as pd
from pandas import Series
import numpy as np
from collections import defaultdict

########## Import csv and remove whitespace

df = pd.read_csv(
'/users/orlando/ds/metis/metisgh/prework/dsp/python/faculty.csv', delimiter=' *, *', engine='python'
)

######### Eliminate all variations of degree names (with and without periods)

df.degree.replace((r"Ph\.*D\.*"), 'PhD', regex=True,inplace=True)
df.degree.replace((r"Sc\.*D\.*"), 'ScD', regex=True,inplace=True)
df.degree.replace((r"M\.*S\.*"), 'MS', regex=True,inplace=True)

########################### Create list of unique last names


unique = (sorted(list(set(x.split(' ')[-1] for x in df['name']))))


######################## Create list of  3 other columns

degrees = df['degree'].tolist()
titles = df['title'].tolist()
emails = df['email'].tolist()

combined = []

for x in range(len(unique)):
    new = [degrees[x], titles[x], emails[x]]
    combined.append(new)
 


######create new dataframe with "lastname, degree, title, email"

df2 = df.copy()

df2['name'] = df2['name'].apply(lambda x: x.split(' ')[-1])

mydict =  defaultdict(list)

for x in range(len(df2['name'])):
	key = df2['name'][x]
	mydict[key].append([df2['degree'][x], df2['title'][x], df2['email'][x]])

print("Quetion 6 --------------------------------------------")

first3valuess = {k: mydict[k] for k in sorted(mydict.keys())[:3]}
print(first3valuess)
############################# Create list of (first name, last name)



first_last = [(x.split(' ')[0], x.split(' ')[-1]) for x in df['name']]

	
dic_names = dict(zip(first_last,combined))

print("Question 7 ------------------------------------------")


first3vals = {k: dic_names[k] for k in sorted(dic_names.keys())[:3]}
print(first3vals)

    
 ############################## Create list of (last name, first name)   


last_first = [(x.split(' ')[-1],x.split(' ')[0]) for x in df['name']]
	
dic_lastN = dict(zip(last_first,combined))


print('Question 8 -------------------------------------------')
for x in dic_lastN.items():
	print(x)