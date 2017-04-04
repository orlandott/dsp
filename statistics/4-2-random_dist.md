[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```

from __future__ import print_function, division


import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot
import random
import matplotlib

randint = np.random.random(1000)


pmf = thinkstats2.Pmf(randint)
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Random integer', ylabel='PMF')
thinkplot.show()

cdf = thinkstats2.Cdf(randint)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random integer', ylabel='CDF')
thinkplot.show()

```

When I try to print the PMF for the random numbers between 1 and 1000 the result is a solid box of lines. The probability for every number creates a full graph that can't be used to differentiate between different numbers. 

On the other hand, the CDF gives us a solitd line diagonally across the graph, meaning the distribution is uniform.