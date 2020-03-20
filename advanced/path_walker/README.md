# PathWalker Exercise

## Goals

1. Learning about the `os` module
2. Practicing using mocks in unit tests
3. Learning about OOP and writing a best-practiced class

## Introduction

In this exercise, you'll implement several ways to traverse over your computer's filesystem.

The first way is via the `os` module, which serves as a bridge for common operating system actions.

The second way also use the `os` module, but via a class named `PathWalker` that you'll implement yourself.
The class should be a good example for the object oriented programming (OOP) contept.

You must write good unit tests. The tests should be ablel to run on every computer, and not be dependent on your machine.
Also, the code should be cross-platform, meaning it need to support both Windows and Unix-based operating systems.

> :warning: Consulting with others regarding technical work is generally a good idea. With regular work, it's encouraged to pair programming and helping each other.
  **However**, when it comes to learning a language, this is not the case. Attempting to tackle exercises alone is a hugh part of learning, even if the result is not perfect. If you'll get something wrong, the reviewer will let you know.
  Please refrain from consulting with others when working on training exercises.

## The Interface

### Directory traversal

Write a recursive function that uses the `os` module to traverse over the filesystem tree, and print the names of all files and directories in the same tree.

For example:

```
>>> recurse_files(r"C:\Program Files\Common Files")
C:\Program Files\Common Files\Adobe
C:\Program Files\Common Files\Crystal Decisions
C:\Program Files\Common Files\Designer
...
```

> :pencil: The `os` module provides several ways to know if a specific path points to a file or a directory.
> Read the module's documentation to find out the simplest solution

### The `PathWalker` class

Write a class named `PathWalker` that manages a pathname:

```
>>> walker = PathWalker(r"C:\Program Files\Common Files")
```

The class should implement the `__repr__` and `__str__` methods like so:

```
>>> print(repr(walker))
PathWalker("C:\\Program Files\\Common Files")
>>> print(walker)
C:\\Program Files\\Common Files
```

The class should implement the `__getitem__` method so that you can access the walker's decendents:

```
>>> print(repr(walker["Microsoft Shared"]))
PathWalker("C:\\Program Files\\Common Files\\Microsoft Shared")
>>> print(repr(walker[".."]))
PathWalker("C:\\Program Files")
```

The class should implement `__iter__` in a way that yields contained files and directories:

```
>>> for subwalker in walker:
...     print(subwalker)
...
"C:\\Program Files\\Common Files\\Adobe"
"C:\\Program Files\\Common Files\\Crystal Decisions"
"C:\\Program Files\\Common Files\\Designer"
...
```

Implement the `recurse_files` function using the `PathWalker` class:

```
>>> recurse_files(PathWalker(r"C:\Program Files\Common Files"))
```

## Recommendations

* Of course, use the `os` module for implementing the code and for being compatible with any platform
* For the tests, you should take a look at `unittest.mock`
