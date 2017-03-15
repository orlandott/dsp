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


####################### Creating dummy variables for each of the degrees
###################### (in order to be able to have more analytical capabilities)


    
df['PhD'] = 0
n = 0
for x in df['degree']:
    if 'PhD' in x:
        df['PhD'][n] = 1
    else:
        df['PhD'][n] = 0
    n += 1

df['ScD'] = 0
n = 0
for x in df['degree']:
    if 'ScD' in x:
        df['ScD'][n] = 1
    else:
        df['ScD'][n] = 0
    n += 1

df['MD'] = 0
n = 0
for x in df['degree']:
    if 'MD' in x:
        df['MD'][n] = 1
    else:
        df['MD'][n] = 0
    n += 1

df['MPH'] = 0
n = 0
for x in df['degree']:
    if 'MPH' in x:
        df['MPH'][n] = 1
    else:
        df['MPH'][n] = 0
    n += 1       

df['MS'] = 0
n = 0
for x in df['degree']:
    if 'MS' in x:
        df['MS'][n] = 1
    else:
        df['MS'][n] = 0
    n += 1

df['B.S.Ed.'] = 0
n = 0
for x in df['degree']:
    if 'B.S.Ed.' in x:
        df['B.S.Ed.'][n] = 1
    else:
        df['B.S.Ed.'][n] = 0
    n += 1

df['JD'] = 0
n = 0
for x in df['degree']:
    if 'JD' in x:
        df['JD'][n] = 1
    else:
        df['JD'][n] = 0
    n += 1

###################################Printing total number of degrees 



print("-------Question 1: Total number of Degrees-------------")
print('PhD:', df['PhD'].sum())
print('ScD:', df['ScD'].sum())
print('MD:', df['MD'].sum())
print('MPH:', df['MPH'].sum())
print('MS:', df['MS'].sum())
print('B.S.Ed.:', df['B.S.Ed.'].sum())
print('JD:', df['JD'].sum())


################################ Printing total number of titles

#### Rename incorrect title
df['title'][24] = "Assistant Professor of Biostatistics"

print("-------Question 2: Total number of titles-------------")
print(df.title.value_counts())

######################################### Putting emails in a list

emails = []

for x in df['email']:
    emails.append(x)

print('---------Question 3: List of Emails------------------------')
for x in emails:
    print(x)
    
################################### Counting email domains

df['domain'] = 0

print('---------Question 4: List of Unique Domains------------------------')
domains = []
for x in emails:
    new = x.split('@')
    domains.append(new[1])
unique_domains= set(domains)

for x in unique_domains:
    print(x)
    
