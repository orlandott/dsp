[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

 Using the following built-in Cohen's D calculator from ThinkStats:



    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d



Calling the function:


 CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

  
   -0.0886729270726




This result is negative, indicating that first babies are a little lighter. However, a "small" effect from a Cohen's D 
calculation would be 0.2. "Medium" effects tend to be 0.5 or larger and "large" effects are 0.8 or larger.
Since the effect in this size is less than half the value of a "small" effect, we can be confident it is not statistically 
significant. To sum up, the difference between the means of two groups divided by the pooled standard deviation is not enough
for us to assert that there is a significant difference.