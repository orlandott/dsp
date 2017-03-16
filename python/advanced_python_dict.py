import re
import pandas as pd
from pandas import Series
import numpy as np

########## Import csv and remove whitespace

df = pd.read_csv(
'/users/orlando/ds/metis/metisgh/prework/dsp/python/faculty.csv', delimiter=' *, *', engine='python'
)

######### Eliminate all variations of degree names (with and without periods)

df.degree.replace((r"Ph\.*D\.*"), 'PhD', regex=True,inplace=True)
df.degree.replace((r"Sc\.*D\.*"), 'ScD', regex=True,inplace=True)
df.degree.replace((r"M\.*S\.*"), 'MS', regex=True,inplace=True)

#########################################

df['surname'] = 0
surname = []
for x in df['name']:
	name = x.split(' ')
	surname.append(name[-1])
	df['surname'][x] = surname

print (df['surname'])
