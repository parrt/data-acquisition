# Matrices in Python

A matrix is a (often) two-dimensional data structure that we can represent as a list of lists and Python. For example, the identity matrix looks like the following, which has all zeros except for the diagonal, which is all ones:

```python
A = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
```

To get a specific row, we index with one value:

```python
print A[0] # [1, 0, 0]
print A[1] # [0, 1, 0]
```

If we want a specific element at a row and column, we use notation `A[row][col]`. For example, we could say that all `A[i][j]==1` for `i==j` in the identity matrix.

Perhaps more commonly in this class, we will use the list of list data structure to record rows of columnar data.

```python
data = [['2016-08-12', 'parrt', 3.1],
        ['2016-08-13', 'tombu', 4.3]]
```

To access individual elements we will very commonly see a nested loop structure in the code like this:

```python
for row in data:
	for col in row:
		print col # print each element on line by itself
```

Another way to iterate through the elements is with indexing. The following code does the exact same thing.

```python
rows = 2
cols = 3
for i in range(rows):
	for j in range(cols):
		print data[i][j]
```

