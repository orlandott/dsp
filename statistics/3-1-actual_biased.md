[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```
from __future__ import print_function, division

import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot
import matplotlib

resp = nsfg.ReadFemResp()

pmf2 = thinkstats2.Pmf(resp.numkdhh, label='actual numkidhh')

thinkplot.Hist(pmf2)
thinkplot.Config(xlabel='Number of kids in household)', ylabel='Pmf')
thinkplot.show()

hist2 = thinkstats2.Hist(resp.numkdhh, label='numkidhh')
thinkplot.Hist(hist2)
thinkplot.Config(xlabel='Number of kids in household)', ylabel='Count')
thinkplot.show()

def BiasPmf(pmf2, label):
    new_pmf = pmf2.Copy(label=label)

    for x, p in pmf2.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biased_pmf = BiasPmf(pmf2, label='observed numkidhh')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf2, biased_pmf])
thinkplot.Config(xlabel='Number of kids', ylabel='PMF') 
thinkplot.show()

print('Actual mean', pmf2.Mean())
print('Observed mean', biased_pmf.Mean())

```

There is very large difference between the biased and the unbiased mean. The actual number of children per family(1.02) 
is actually less than half what we would observe if we asked the children (2.4). The reason for this is that there are no 
'zero-children family' children that we would have encountered in the survey.  