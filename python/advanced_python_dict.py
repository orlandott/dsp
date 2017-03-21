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


names = df['name'].tolist()
surnames = []
for x in names:
	name = x.split(' ')
	surnames.append(name[-1])
	
unique = sorted(list(set(surnames)))


######################## Create list of  3 other columns

degrees = df['degree'].tolist()
titles = df['title'].tolist()
emails = df['email'].tolist()

combined = []

for x in range(len(unique)):
    new = [degrees[x], titles[x], emails[x]]
    combined.append(new)
 


######################## Merge last names with other columns

# dicf = defaultdict(list, zip(unique,combined))


# #d1 = defaultdict(list, zip(unique,combined))

# for k, v in dicf:
#     d1[k].append(v)

# d = dict((k, tuple(v)) for k, v in d1.items())


# print('Question 6 ---------------------------------------------')
# q6_ordered_keys = sorted(unique)
# for i in range(16):
# 	print(q6_ordered_keys[i], ': ', d[q6_ordered_keys[i]])
    



############################## Create list of (first name, last name)

names = df['name'].tolist()
first_last = []
for x in names:
	name = x.split(' ')
	first_last.append((name[0],name[-1]))
	
dic_names = dict(zip(first_last,combined))

print("Question 7 ------------------------------------------")
# for x in dic_names:
#     print(x, dic_names[x])

first3vals = {k: dic_names[k] for k in sorted(dic_names.keys())[:3]}
print(first3vals)
		
    
 ############################## Create list of (last name, first name)   

names = df['name'].tolist()
last_first = []
for x in names:
	name = x.split(' ')
	last_first.append((name[-1],name[0]))
	
dic_lastN = dict(zip(last_first,combined))


print('Question 8 -------------------------------------------')
for x in dic_lastN.items():
	print(x)