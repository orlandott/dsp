[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

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