# Importing your own code

## Goals

* treat your own existing code like a library
* learn more about testing
* learn about the string `%` operator
* learn rules for when Python allows newlines
* learn not to compare floating-point numbers with `==`
* learn import aliases
* use numpy's `isclose()` function

The end result: `stats.py` and `test_stats.py`.

## Description

To get started, let's create a file called `stats.py` that we will use to hold useful statistics code. Put the following function that computes the average into that file.
 
```python
def mean(x):
    "sum of values / num elements"
    total = 0.0
    N = len(x)
    for v in x:
        total += v
    return total / N
```

Now, let's say we have the following data for player heights of 40 randomly-selected US pro players:

```python
football = [
    6.329999924, 6.5, 6.5, 6.25, 6.5, 6.329999924, 6.25, 6.170000076,
    6.420000076, 6.329999924, 6.420000076, 6.579999924, 6.079999924,
    6.579999924, 6.5, 6.420000076, 6.25, 6.670000076, 5.909999847, 6, 5.829999924,
    6, 5.829999924, 5.079999924, 6.75, 5.829999924, 6.170000076, 5.75, 6, 5.75,
    6.5, 5.829999924, 5.909999847, 5.670000076, 6, 6.079999924, 6.170000076,
    6.579999924, 6.5, 6.25]

basketball = [
    6.079999924, 6.579999924, 6.25, 6.579999924, 6.25, 5.920000076, 7,
    6.409999847, 6.75, 6.25, 6, 6.920000076, 6.829999924, 6.579999924,
    6.409999847, 6.670000076, 6.670000076, 5.75, 6.25, 6.25, 6.5, 6,
    6.920000076, 6.25, 6.420000076, 6.579999924, 6.579999924, 6.079999924, 6.75,
    6.5, 6.829999924, 6.079999924, 6.920000076, 6, 6.329999924, 6.5,
    6.579999924, 6.829999924, 6.5, 6.579999924]
```

Put those definitions into file `test_stats.py`.

To compute the average height, we want to use our existing code but we don't want to cut-and-paste, which is a great sin. All we have to do is use the `import` statement in `test_stats.py` like we did before with `math`:

```python
import stats
```

The only difference is that `stats.py` must be in the same directory as the `test_stats.py` file we are currently building. (Whereas `math.py` is off in some standard location of the disk Python knows to look for.)

```python
import stats

... define football and basketball ...
print "football mean is %f" % stats.mean(football)
print "basketball mean is %f" % stats.mean(basketball)
```

The `%` operator lets you create strings with "holes" in them where values get placed. I get output:

```
football mean is 6.186750
basketball mean is 6.453250
```