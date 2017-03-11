# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples are immutable, lists are not. They are similar in that you can use indices[x] or slices[x:y]to call different objects inside. Lists are enclosed by [] and tuples by (). They also differ in that tuple assignment allows for changing tuple variables without the need of an intermediary variable (a,b = b,a). Tuples can also be used so a function returns more than one value(e.g. divmod function). Tuples will work as keys in a dictionary but lists will not. The short answer for this is that since lists are mutable they don't have a hash function which means they cannot be searched through as efficiently. Keys in a dictionary must be hashable(and thus immutable) so they are accessed more quickly.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and list both are ways of organizing data. However, sets cannot have duplicates. Additionally, sets are unordered. Sets only allow hashable items which means they are faster to look through than lists. Sets can also be used to remove duplicates by converting something into a set. Sets also allow the typical operations from set theory in math like union, intersection, and difference. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is used to pass an anonymous function. It can be used to create a quick function that is only used in that instance. For example, one could use lambda as a function in the key argument as such: 

` sorted(list, key = lambda word: word.lower()) `

another example of lambda is to map or filter a function over a range of numbers:

` cubed = map(lambda x: x**3, range(1,10))
  evens = filter(lambda x: x%2==0, range(1,20))
`

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a way to quickly create lists. For example, instead of having to create a 'for' loop, we can simply create a list by typing 

```
squares = [x**2 for x in range(1,20)]

cubed = [x**3 for x in range(1,10)]

uppercased = [x for x in my_list if x.isupper() == True]
```

using map and filter instead:

```
squaresevens = map(lambda x: x**2, range(1,20))

cubedodds = map(lambda x: x**3, range(1,10)

uppercased = filter(lambda x: x.isupper == True, my_list)
```




---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 907 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





