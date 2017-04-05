[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

print((dist.cdf(185.4) - dist.cdf(177.8))*100)
```

The number of males who are between 5'10 and 6'1 is 34.2%
