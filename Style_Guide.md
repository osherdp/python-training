<!--
AUTHORS:
Yaakov Bareket
-->

# Google Python Style Guide


<a id="1-background"></a>

<a id="background"></a>
## 1 About

This is the a guide for properly writing python code and comments in our unit. Our unit uses google's style guide because it is by far the most readable. I condensed it for you here (I'm not promising that everything you need to know is here but most of it is).


<a id="s2-python-language-rules"></a>
<a id="2-python-language-rules"></a>

<a id="python-language-rules"></a>
## 2 The Basics 

<a id="s2.1-imports"></a>
<a id="21-imports"></a>

<a id="imports"></a>
### 2.1 Imports 

Imports should be in the following order with a line between each group

1. Built-ins (things like os, time)

2. 3rd party libraries (things like waiting and selenium)

3. Local modules

Within each group imports should be in length order.

```python
import os
from time import sleep

import docopt
import waiting

import my_module
from my_other_module import *
```

Finally. Do not use relative names in imports. Even if the module is in the same package,
use the full package name. This helps prevent unintentionally importing a
package twice.


### 2.2 Naming 

We follow some strict rules for variable names.

1. underscores not spaces
```python
good_name = 'Happy Yaakov'
```

```python
badName = 'Sad Igal'

evenworsename = 'Yair will personally ask Fire to give you Shabbat'
```

We also don't use abreviations in our names since they lead to other people not understanding what you meant.


```python
sometimes_names_will_be_long = 1
```

```python
d = {}  # Osher wants you to give your dictionary a name making it clear what is inside

# We even avoid common abbreviations
rec = "recieved content"
res = "my response"
```

Finally, don't include the type in the name. Instead say what the variable is used for
```python
movies_to_watch_on_bidud = ['Lord of the Rings', 'Shawshank Redemption']
```

```python
movie_list = ['You dont get to watch movies if you write code like that']
```

### 2.3 Constants 

If you use a particular number, string etc. that you are hardcoding into the code you generally should use a constant. Constants make it clearer as to why random seeming numbers are in you code and allow you to change them easily.


```python
from time import sleep

WAIT_TIME = 1  # seconds

tell_ido_to_come_back()
sleep(WAIT_TIME)
cry_that_hes_not_back_yet()
sleep(WAIT_TIME)
```

Constants should be all caps and use underscores for spacing.

### 2.4 Unit signaling 

As can be seen in the previous example, when you use a number include a comment to indicate what it refers to (seconds, minutes, trys, nodes)

```python
ARGUMENT_TIME = 30  # minutes per day

haveDumbArguments(ARGUMENT_TIME)
```

Constants should be all caps and use underscores for spacing.

### 2.5 Exceptions Handling 

Do not use generic try/catch blocks. Doing so leads to accidentally catching errors that you didn't mean to and then never finding them. When using try/catch be as specific as possible.

### 2.6 Blank Lines 

Two blank lines between top-level definitions, be they function or class
definitions. One blank line between method definitions and between the `class`
line and the first method. No blank line following a `def` line. Use single
blank lines as you judge appropriate within functions or methods.

<a id="s2.5-whitespace"></a>
<a id="25-whitespace"></a>

<a id="whitespace"></a>

### 2.7 Whitespace 

Follow standard typographic rules for the use of spaces around punctuation.

No whitespace inside parentheses, brackets or braces.

```python
Yes: eat(fruits[1], {salad: 2}, [])
```

```python
No:  eat( fruits[ 1 ], { salad: 2 }, [ ] )
```

No whitespace before a comma, semicolon, or colon. Do use whitespace after a
comma, semicolon, or colon, except at the end of the line.

```python
Yes: if value_1 == 4:
         print(value_1, value_2)
     final_1, final_2 = value_1, value_2
```

```python
No:  if value_1 == 4 :
         print(value_1 , value_2)
     final1 , final_2 = value_1 , value_2
```

No whitespace before the open paren/bracket that starts an argument list,
indexing or slicing.

```python
Yes: gigi(1)
```

```python
No:  gigi (1)
```


```python
Yes: dogs['fastest'] = animals[index]
```

```python
No:  dogs ['fastest'] = animals [index]
```

No trailing whitespace.

Surround operators with a single space on either side for assignment
(`=`), comparisons (`==, <, >, !=, <>, <=, >=, in, not in, is, is not`), and
Booleans (`and, or, not`). 

```python
Yes: value == 1
```

```python
No:  value<1
```

The exception is when passing keyword arguments or defining a default
parameter value in which case you should not use a whitespace 

```python
Yes:
def complex(real, imaginary=0.0): 
    return Magic(real=2, imaginary=3)
```

```python
No:  
def complex(real, imag = 0.0):  
    return Magic(real = 2, imaginary = 3)

No:  
def complex(real, imaginary): 
    return Magic(real =2, imaginary= 3)
```

## 3 Documentation

### 3.1 Module Docstings

Files should start with a docstring describing the contents and usage of the
module.
```python
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  fred = BossMan()
  rescheduled = fred.call_meeting()
"""
```
<a id="s3.1-docstrings"></a>
<a id="31-docstrings"></a>
<a id="docstrings"></a>

<a id="function-docs"></a>
#### 3.2 Functions and Methods 

A function must have a docstring, unless it meets all of the following criteria:

-   not externally visible
-   very short
-   obvious

Functions should be documented as follows

```python
def function_name(argument, other_argument=None):
    """Gives a one line simple present tense description with a period at the end.

    More lines telling you in greater detail what the function does.
    Notice that the comments are all aligned. It is ok for long sentances 
    to wrap around but make sure that there is a period at the end.

    Args:
        argument (type): Description fo the first argument.
        other_argument (type): Description of the second argument.
            if the description is more than one line then it gets indented.
            Note that this is different then the function description.

    Returns:
        (type): A description of the thing that gets returned.
            No need to mention the name of the returned variable since
            that doesn't matter to someone reading the doc. If you return
            multiple values then the type should be "tuple".

    Raises:
        ErrorName: A description of the error and what could cause it.
    """
```

<a id="s3.8.4-comments-in-classes"></a>
<a id="384-classes"></a>
<a id="comments-in-classes"></a>

<a id="class-docs"></a>
#### 3.8.4 Classes 

Classes should have a docstring below the class definition describing the class.
If your class has public attributes, they should be documented here in an
`Attributes` section and follow the same formatting as a
[function's `Args`](#doc-function-args) section.

```python
class SampleClass(object):
    """One line summary of class here.

    Notice that the naming convention for classes is that the first letter 
    of every word is uppercase and there are no spaces or underscores.
    
    Attributes:
        yaakov_funny (bool): Indicates if Yaakov is funny.
        bad_jokes (number): Count of Yaakovs bad jokes
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.yaakov_funny = false
        self.bad_jokes = 20

    def judge_natan(self):
        """Gives Natan mishpat for breaking dress code."""
        pass
```

<a id="comments-in-block-and-inline"></a>
<a id="s3.8.5-comments-in-block-and-inline"></a>
<a id="385-block-and-inline-comments"></a>

<a id="comments"></a>
