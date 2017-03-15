import pandas as pd
from pandas import Series


df = pd.read_csv(
'/users/orlando/ds/metis/metisgh/prework/dsp/python/faculty.csv', delimiter=' *, *', engine='python'
)


emails = []

for x in df['email']:
    emails.append(x)


emails_s = pd.Series(emails)

emails_s.to_csv('/users/orlando/ds/metis/metisgh/prework/dsp/python/emails.csv', index=False)

