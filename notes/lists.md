# Lists and Vectors

Lists are sequences of objects. These are also called arrays.

```python
sizes = [1,2,3,4]
names = ['parrt', 'tombu']
```

Lists can have homogeneous or heterogeneous items.

```python
stuff = ['parrt', 1.2, True]
```

Lists are like books with individual pages. We can also treat the book as a single object: `print names`.

We can concatenate two lists using the addition symbol

```python
[1,2] + [9,10,11] # gives [1, 2, 9, 10, 11]
```

Books are referenced by page number, list elements are referenced by their index number and indexes start at 0 not 1:

```python
names = ['lois', 'stewie', 'peter', 'brian']
names[0] # prints lois
```

## Iterating over a list

```python
for name in names:
        print name
```

We do that a lot as well as walking lines of text.

```python
text = """lois,34
peter,33
brian,10
"""
lines = text.split("\n") # split into different lines
for line in lines:
	cols = line.split(',') # split into different columns
	print cols
```

Sometimes we want to iterate a variable, `i`, from 0 to the length of a list - 1. It is such a common pattern that almost all languages have something to automate this boilerplate code for us. Python has `range()`:

```python
n = 5
print range(0,5) # gives [0, 1, 2, 3, 4]
for i in range(5): # range(5) == range(0,5)
    print i, # comma on the end of a print means no \n
print # print with no arguments simply gives a \n
```

That prints `0 1 2 3 4`.

**Exercise**

Write a program that counts the number of `A`’s (scores between 90 and 100)

```python
grades = [90,100,70,45,76,84,93,21,36,99,100]
numA = 0
for grade in grades:
	# if grade is in 90-100, add one to numA

print "Number of A's: %d" % numA
```

## Adding to a list

A very common operation is to iterate through one bit of data and collect info in a list.

```python
sizes = [1,2,3,4]
bigger = []
for size in sizes:
    bigger.append(s*size)
print bigger # [2,4,6,8]
```

Or, as a convenience, you can do:

```python
sizes = [1,2,3,4]
bigger = [2*size for size in sizes]
```

That is also useful for lists of strings:

```python
names = ['lois', 'stewie', 'peter', 'brian']
upper = [name.upper() for name in names]
print upper # ['LOIS', 'STEWIE', 'PETER', 'BRIAN']
```

## Iterating through strings

Strings act like arrays/lists too. ``

```python
s="hi, mom"
print s[0] # prints 'h'
print s[2] # prints ','
for c in s:
	print c  # prints 1 char from s each iteration per line
```