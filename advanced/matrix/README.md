# Matric Exercise

## Goals

1. OOP
2. The object class
3. List comprehension

## Introduction

The purpose of this exercise is to implement class for the datatype `Matrix` which has the following characteristics:

* Immutable - you can't change an instance of this class after its initialization (like the `tuple` type)
* We only deal with squared matrices (the dimensions are always `n * n`).
* The matrix supports addition, subtraction, multiplication by scalar and matrices multiplication.
* The matrix can represent itself via the `repr()` function.
* List comprehension usage is recommended where appropriate.

> :warning: Consulting with others regarding technical work is generally a good idea. With regular work, it's encouraged to pair programming and helping each other.
  **However**, when it comes to learning a language, this is not the case. Attempting to tackle exercises alone is a hugh part of learning, even if the result is not perfect. If you'll get something wrong, the reviewer will let you know.
  Please refrain from consulting with others when working on training exercises.

> :warning: DO NOT use `numpy` library when doing this exercise. You may use it in general :)

## Interface

You can initialize the matrix using a `tuple` of `tuple`s:

```
>>> a = Matrix((1, 2), (3, 4))
>>> b = Matrix((3, 5), (6, 8))
```

or represent it via the `repr()` function, and printing it via `str()`:

```
>>> a
Matrix((1, 2), (3, 4))
>>> print(a)
((1, 2), (3, 4))
```

Define a property which displays the matrix as a tuple:

```
>>> a.tuples
((1, 2), (3, 4))
```

> :pencil: You can read about properties using `help(property)` in any Python shell.

Enable creation of the unity matrix (ones on the main diagonal and all the rest are zeros), using a `classmethod`:

```
>>> Matrix.unity(2)
Matrix(((1, 0), (0, 1)))
>>> Matrix.unity(3)
Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
```

Another `classmethod` that creates a matrix which is full of ones:

```
>>> Matrix.ones(3)
Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1)))
```

> :pencil:
  If you are not familiar with matrix multiplication operation, it probably doesn't work as you think.
  Read about it somewhere before implementing it.

Multiplication:

```
>>> a * b
Matrix(((15, 21), (33, 47)))
```

Addition:

```
>>> a + Matrix.unity(2)
Matrix(((2, 2), (3, 5)))
```

Subtraction:

```
>>> a - b
Matrix(((-2, -3), (-3, -4)))
```

Multiplication by scalar:

```
>>> a * 10
Matrix(((10, 20), (30, 40)))
>>> 10 * a
Matrix(((10, 20), (30, 40)))
```

Division by scalar:

```
>>> a / 10
Matrix(((0.1, 0.2), (0.3, 0.4)))
```

Comparision:

```
>>> a != b
True
>>> a == b
False
```

Iteration over its lines:

```
>>> for line in a:
        print(line)
(1, 2)
(3, 4)
```

Support of getting a `hash()` value, so that a matrix can be a key in dictionary, or a set's item:

```
>>> dictionary = {}
>>> dictionary[Matrix(((1, 1), (2, 2)))] = 1
>>> dictionary[Matrix(((1, 1), (2, 2)))] = 2
>>> dictionary[Matrix(((1, 1), (2, 3)))] = 3
>>> dictionary
{Matrix(((1, 1), (2, 2))): 2, Matrix(((1, 1), (2, 3))): 3}
```

Pay attention that the second insertion has overriden the first one, because the `hash()` function returned the same value.
