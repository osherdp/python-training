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

### 2.2 Constants 

If you use a particular number, string etc. that you are hardcoding into the code you generally should use a constant. Constants make it clearer as to why random seeming numbers are in you code and allow you to change them easily.


```python
from time import sleep

WAIT_TIME = 1  # seconds

doSomething()
sleep(WAIT_TIME)
doSometingElse()
sleep(WAIT_TIME)
```

Constants should be all caps and use underscores for spacing.

### 2.3 Unit signaling 

As can be seen in the previous example, when you use a number include a comment to indicate what it refers to (seconds, minutes, trys, nodes)

```python
TIMEOUT = 1  # minute

doSomethingRepeatedly(TIMEOUT)
```

Constants should be all caps and use underscores for spacing.

### 2.4 Exceptions Handling 

Do not use generic try/catch blocks. Doing so leads to accidentally catching errors that you didn't mean to and then never finding them. When using try/catch be as specific as possible.

### 2.5 Blank Lines 

Two blank lines between top-level definitions, be they function or class
definitions. One blank line between method definitions and between the `class`
line and the first method. No blank line following a `def` line. Use single
blank lines as you judge appropriate within functions or methods.

<a id="s2.5-whitespace"></a>
<a id="25-whitespace"></a>

<a id="whitespace"></a>

### 2.6 Whitespace 

Follow standard typographic rules for the use of spaces around punctuation.

No whitespace inside parentheses, brackets or braces.

```python
Yes: spam(ham[1], {eggs: 2}, [])
```

```python
No:  spam( ham[ 1 ], { eggs: 2 }, [ ] )
```

No whitespace before a comma, semicolon, or colon. Do use whitespace after a
comma, semicolon, or colon, except at the end of the line.

```python
Yes: if x == 4:
         print(x, y)
     x, y = y, x
```

```python
No:  if x == 4 :
         print(x , y)
     x , y = y , x
```

No whitespace before the open paren/bracket that starts an argument list,
indexing or slicing.

```python
Yes: spam(1)
```

```python
No:  spam (1)
```


```python
Yes: dict['key'] = list[index]
```

```python
No:  dict ['key'] = list [index]
```

No trailing whitespace.

Surround operators with a single space on either side for assignment
(`=`), comparisons (`==, <, >, !=, <>, <=, >=, in, not in, is, is not`), and
Booleans (`and, or, not`). 

```python
Yes: x == 1
```

```python
No:  x<1
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

### 3.1 Docstings

Files should start with a docstring describing the contents and usage of the
module.
```python
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```
<a id="s3.1-functions-and-methods"></a>
<a id="31-functions-and-methods"></a>
<a id="functions-and-methods"></a>

<a id="function-docs"></a>
#### 3.8.3 Functions and Methods 

In this section, "function" means a method, function, or generator.

A function must have a docstring, unless it meets all of the following criteria:

-   not externally visible
-   very short
-   obvious

A docstring should give enough information to write a call to the function
without reading the function's code. The docstring should be descriptive-style
(`"""Fetches rows from a Bigtable."""`) rather than imperative-style (`"""Fetch
rows from a Bigtable."""`), except for `@property` data descriptors, which
should use the <a href="#384-classes">same style as attributes</a>. A docstring
should describe the function's calling syntax and its semantics, not its
implementation. For tricky code, comments alongside the code are more
appropriate than using docstrings.

A method that overrides a method from a base class may have a simple docstring
sending the reader to its overridden method's docstring, such as `"""See base
class."""`. The rationale is that there is no need to repeat in many places
documentation that is already present in the base method's docstring. However,
if the overriding method's behavior is substantially different from the
overridden method, or details need to be provided (e.g., documenting additional
side effects), a docstring with at least those differences is required on the
overriding method.

Certain aspects of a function should be documented in special sections, listed
below. Each section begins with a heading line, which ends with a colon. All
sections other than the heading should maintain a hanging indent of two or four
spaces (be consistent within a file). These sections can be omitted in cases
where the function's name and signature are informative enough that it can be
aptly described using a one-line docstring.

<a id="doc-function-args"></a>
[*Args:*](#doc-function-args)
:   List each parameter by name. A description should follow the name, and be
    separated by a colon and a space. If the description is too long to fit on a
    single 80-character line, use a hanging indent of 2 or 4 spaces (be
    consistent with the rest of the file).

    The description should include required type(s) if the code does not contain
    a corresponding type annotation. If a function accepts `*foo` (variable
    length argument lists) and/or `**bar` (arbitrary keyword arguments), they
    should be listed as `*foo` and `**bar`.

<a id="doc-function-returns"></a>
[*Returns:* (or *Yields:* for generators)](#doc-function-returns)
:   Describe the type and semantics of the return value. If the function only
    returns None, this section is not required. It may also be omitted if the
    docstring starts with Returns or Yields (e.g. `"""Returns row from Bigtable
    as a tuple of strings."""`) and the opening sentence is sufficient to
    describe return value.

<a id="doc-function-raises"></a>
[*Raises:*](#doc-function-raises)
:   List all exceptions that are relevant to the interface. You should not
    document exceptions that get raised if the API specified in the docstring is
    violated (because this would paradoxically make behavior under violation of
    the API part of the API).

```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
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
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```

<a id="comments-in-block-and-inline"></a>
<a id="s3.8.5-comments-in-block-and-inline"></a>
<a id="385-block-and-inline-comments"></a>

<a id="comments"></a>
#### 3.8.5 Block and Inline Comments 

The final place to have comments is in tricky parts of the code. If you're going
to have to explain it at the next [code
review](http://en.wikipedia.org/wiki/Code_review), you should comment it
now. Complicated operations get a few lines of comments before the operations
commence. Non-obvious ones get comments at the end of the line.

```python
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.

if i & (i-1) == 0:  # True if i is 0 or a power of 2.
```

To improve legibility, these comments should start at least 2 spaces away from
the code with the comment character `#`, followed by at least one space before
the text of the comment itself.

On the other hand, never describe the code. Assume the person reading the code
knows Python (though not what you're trying to do) better than you do.

```python
# BAD COMMENT: Now go through the b array and make sure whenever i occurs
# the next element is i+1
```

<!-- The next section is copied from the C++ style guide. -->

<a id="s3.8.6-punctuation-spelling-and-grammar"></a>
<a id="386-punctuation-spelling-and-grammar"></a>
<a id="spelling"></a>
<a id="punctuation"></a>
<a id="grammar"></a>

<a id="punctuation-spelling-grammar"></a>
#### 3.8.6 Punctuation, Spelling, and Grammar 

Pay attention to punctuation, spelling, and grammar; it is easier to read
well-written comments than badly written ones.

Comments should be as readable as narrative text, with proper capitalization and
punctuation. In many cases, complete sentences are more readable than sentence
fragments. Shorter comments, such as comments at the end of a line of code, can
sometimes be less formal, but you should be consistent with your style.

Although it can be frustrating to have a code reviewer point out that you are
using a comma when you should be using a semicolon, it is very important that
source code maintain a high level of clarity and readability. Proper
punctuation, spelling, and grammar help with that goal.

<a id="s3.9-classes"></a>
<a id="39-classes"></a>

<a id="classes"></a>
### 3.9 Classes 

If a class inherits from no other base classes, explicitly inherit from
`object`. This also applies to nested classes.

```python
Yes: class SampleClass(object):
         pass


     class OuterClass(object):

         class InnerClass(object):
             pass


     class ChildClass(ParentClass):
         """Explicitly inherits from another class already."""

```

```python
No: class SampleClass:
        pass


    class OuterClass:

        class InnerClass:
            pass
```

Inheriting from `object` is needed to make properties work properly in Python 2
and can protect your code from potential incompatibility with Python 3. It also
defines special methods that implement the default semantics of objects
including `__new__`, `__init__`, `__delattr__`, `__getattribute__`,
`__setattr__`, `__hash__`, `__repr__`, and `__str__`.

<a id="s3.10-strings"></a>
<a id="310-strings"></a>

<a id="strings"></a>
### 3.10 Strings 

Use the `format` method or the `%` operator for formatting strings, even when
the parameters are all strings. Use your best judgment to decide between `+` and
`%` (or `format`) though.

```python
Yes: x = a + b
     x = '%s, %s!' % (imperative, expletive)
     x = '{}, {}'.format(first, second)
     x = 'name: %s; score: %d' % (name, n)
     x = 'name: {}; score: {}'.format(name, n)
     x = f'name: {name}; score: {n}'  # Python 3.6+
```

```python
No: x = '%s%s' % (a, b)  # use + in this case
    x = '{}{}'.format(a, b)  # use + in this case
    x = first + ', ' + second
    x = 'name: ' + name + '; score: ' + str(n)
```

Avoid using the `+` and `+=` operators to accumulate a string within a loop.
Since strings are immutable, this creates unnecessary temporary objects and
results in quadratic rather than linear running time. Instead, add each
substring to a list and `''.join` the list after the loop terminates (or, write
each substring to a `io.BytesIO` buffer).

```python
Yes: items = ['<table>']
     for last_name, first_name in employee_list:
         items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
     items.append('</table>')
     employee_table = ''.join(items)
```

```python
No: employee_table = '<table>'
    for last_name, first_name in employee_list:
        employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
    employee_table += '</table>'
```

Be consistent with your choice of string quote character within a file. Pick `'`
or `"` and stick with it. It is okay to use the other quote character on a
string to avoid the need to `\\ ` escape within the string.

```python
Yes:
  Python('Why are you hiding your eyes?')
  Gollum("I'm scared of lint errors.")
  Narrator('"Good!" thought a happy Python reviewer.')
```

```python
No:
  Python("Why are you hiding your eyes?")
  Gollum('The lint. It burns. It burns us.')
  Gollum("Always the great lint. Watching. Watching.")
```

Prefer `"""` for multi-line strings rather than `'''`. Projects may choose to
use `'''` for all non-docstring multi-line strings if and only if they also use
`'` for regular strings. Docstrings must use `"""` regardless.

Multi-line strings do not flow with the indentation of the rest of the program.
If you need to avoid embedding extra space in the string, use either
concatenated single-line strings or a multi-line string with
[`textwrap.dedent()`](https://docs.python.org/3/library/textwrap.html#textwrap.dedent)
to remove the initial space on each line:

```python
  No:
  long_string = """This is pretty ugly.
Don't do this.
"""
```

```python
  Yes:
  long_string = """This is fine if your use case can accept
      extraneous leading spaces."""
```

```python
  Yes:
  long_string = ("And this is fine if you can not accept\n" +
                 "extraneous leading spaces.")
```

```python
  Yes:
  long_string = ("And this too is fine if you can not accept\n"
                 "extraneous leading spaces.")
```

```python
  Yes:
  import textwrap

  long_string = textwrap.dedent("""\
      This is also fine, because textwrap.dedent()
      will collapse common leading spaces in each line.""")
```

<a id="s3.11-files-and-sockets"></a>
<a id="311-files-and-sockets"></a>
<a id="files-and-sockets"></a>

<a id="files"></a>
### 3.11 Files and Sockets 

Explicitly close files and sockets when done with them.

Leaving files, sockets or other file-like objects open unnecessarily has many
downsides:

-   They may consume limited system resources, such as file descriptors. Code
    that deals with many such objects may exhaust those resources unnecessarily
    if they're not returned to the system promptly after use.
-   Holding files open may prevent other actions such as moving or deleting
    them.
-   Files and sockets that are shared throughout a program may inadvertently be
    read from or written to after logically being closed. If they are actually
    closed, attempts to read or write from them will throw exceptions, making
    the problem known sooner.

Furthermore, while files and sockets are automatically closed when the file
object is destructed, tying the lifetime of the file object to the state of the
file is poor practice:

-   There are no guarantees as to when the runtime will actually run the file's
    destructor. Different Python implementations use different memory management
    techniques, such as delayed Garbage Collection, which may increase the
    object's lifetime arbitrarily and indefinitely.
-   Unexpected references to the file, e.g. in globals or exception tracebacks,
    may keep it around longer than intended.

The preferred way to manage files is using the ["with"
statement](http://docs.python.org/reference/compound_stmts.html#the-with-statement):

```python
with open("hello.txt") as hello_file:
    for line in hello_file:
        print(line)
```

For file-like objects that do not support the "with" statement, use
`contextlib.closing()`:

```python
import contextlib

with contextlib.closing(urllib.urlopen("http://www.python.org/")) as front_page:
    for line in front_page:
        print(line)
```

<a id="s3.12-todo-comments"></a>
<a id="312-todo-comments"></a>

<a id="todo"></a>
### 3.12 TODO Comments 

Use `TODO` comments for code that is temporary, a short-term solution, or
good-enough but not perfect.

A `TODO` comment begins with the string `TODO` in all caps and a parenthesized
name, e-mail address, or other identifier
of the person or issue with the best context about the problem. This is followed
by an explanation of what there is to do.

The purpose is to have a consistent `TODO` format that can be searched to find
out how to get more details. A `TODO` is not a commitment that the person
referenced will fix the problem. Thus when you create a
`TODO`, it is almost always your name
that is given.

```python
# TODO(kl@gmail.com): Use a "*" here for string repetition.
# TODO(Zeke) Change this to use relations.
```

If your `TODO` is of the form "At a future date do something" make sure that you
either include a very specific date ("Fix by November 2009") or a very specific
event ("Remove this code when all clients can handle XML responses.").

<a id="s3.13-imports-formatting"></a>
<a id="313-imports-formatting"></a>

<a id="imports-formatting"></a>
### 3.13 Imports formatting 

Imports should be on separate lines.

E.g.:

```python
Yes: import os
     import sys
```

```python
No:  import os, sys
```


Imports are always put at the top of the file, just after any module comments
and docstrings and before module globals and constants. Imports should be
grouped from most generic to least generic:

1.  Python future import statements. For example:

    ```python
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    ```

    See [above](#from-future-imports) for more information about those.

2.  Python standard library imports. For example:

    ```python
    import sys
    ```

3.  [third-party](https://pypi.org/) module
    or package imports. For example:

    
    ```python
    import tensorflow as tf
    ```

4.  Code repository
    sub-package imports. For example:

    
    ```python
    from otherproject.ai import mind
    ```

5.  **Deprecated:** application-specific imports that are part of the same
    top level
    sub-package as this file. For example:

    
    ```python
    from myproject.backend.hgwells import time_machine
    ```

    You may find older Google Python Style code doing this, but it is no longer
    required. **New code is encouraged not to bother with this.** Simply treat
    application-specific sub-package imports the same as other sub-package
    imports.

    
Within each grouping, imports should be sorted lexicographically, ignoring case,
according to each module's full package path. Code may optionally place a blank
line between import sections.

```python
import collections
import queue
import sys

from absl import app
from absl import flags
import bs4
import cryptography
import tensorflow as tf

from book.genres import scifi
from myproject.backend.hgwells import time_machine
from myproject.backend.state_machine import main_loop
from otherproject.ai import body
from otherproject.ai import mind
from otherproject.ai import soul

# Older style code may have these imports down here instead:
#from myproject.backend.hgwells import time_machine
#from myproject.backend.state_machine import main_loop
```


<a id="s3.14-statements"></a>
<a id="314-statements"></a>

<a id="statements"></a>
### 3.14 Statements 

Generally only one statement per line.

However, you may put the result of a test on the same line as the test only if
the entire statement fits on one line. In particular, you can never do so with
`try`/`except` since the `try` and `except` can't both fit on the same line, and
you can only do so with an `if` if there is no `else`.

```python
Yes:

  if foo: bar(foo)
```

```python
No:

  if foo: bar(foo)
  else:   baz(foo)

  try:               bar(foo)
  except ValueError: baz(foo)

  try:
      bar(foo)
  except ValueError: baz(foo)
```

<a id="s3.15-access-control"></a>
<a id="315-access-control"></a>
<a id="access-control"></a>

<a id="accessors"></a>
### 3.15 Accessors 

If an accessor function would be trivial, you should use public variables
instead of accessor functions to avoid the extra cost of function calls in
Python. When more functionality is added you can use `property` to keep the
syntax consistent.

On the other hand, if access is more complex, or the cost of accessing the
variable is significant, you should use function calls (following the
[Naming](#s3.16-naming) guidelines) such as `get_foo()` and
`set_foo()`. If the past behavior allowed access through a property, do not
bind the new accessor functions to the property. Any code still attempting to
access the variable by the old method should break visibly so they are made
aware of the change in complexity.

<a id="s3.16-naming"></a>
<a id="316-naming"></a>

<a id="naming"></a>
### 3.16 Naming 

`module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`,
`function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`,
`function_parameter_name`, `local_var_name`.


Function names, variable names, and filenames should be descriptive; eschew
abbreviation. In particular, do not use abbreviations that are ambiguous or
unfamiliar to readers outside your project, and do not abbreviate by deleting
letters within a word.

Always use a `.py` filename extension. Never use dashes.

<a id="s3.16.1-names-to-avoid"></a>
<a id="3161-names-to-avoid"></a>

<a id="names-to-avoid"></a>
#### 3.16.1 Names to Avoid 

-   single character names except for counters or iterators. You may use "e" as
    an exception identifier in try/except statements.
-   dashes (`-`) in any package/module name
-   `__double_leading_and_trailing_underscore__` names (reserved by Python)

<a id="s3.16.2-naming-conventions"></a>
<a id="3162-naming-convention"></a>

<a id="naming-conventions"></a>
#### 3.16.2 Naming Conventions 

-   "Internal" means internal to a module, or protected or private within a
    class.

-   Prepending a single underscore (`_`) has some support for protecting module
    variables and functions (not included with `from module import *`). While
    prepending a double underscore (`__` aka "dunder") to an instance variable
    or method effectively makes the variable or method private to its class
    (using name mangling) we discourage its use as it impacts readability and
    testability and isn't *really* private.

-   Place related classes and top-level functions together in a
    module.
    Unlike Java, there is no need to limit yourself to one class per module.

-   Use CapWords for class names, but lower\_with\_under.py for module names.
    Although there are some old modules named CapWords.py, this is now
    discouraged because it's confusing when the module happens to be named after
    a class. ("wait -- did I write `import StringIO` or `from StringIO import
    StringIO`?")

-   Underscores may appear in *unittest* method names starting with `test` to
    separate logical components of the name, even if those components use
    CapWords. One possible pattern is `test<MethodUnderTest>_<state>`; for
    example `testPop_EmptyStack` is okay. There is no One Correct Way to name
    test methods.

<a id="s3.16.3-file-naming"></a>
<a id="3163-file-naming"></a>

<a id="file-naming"></a>
#### 3.16.3 File Naming 

Python filenames must have a `.py` extension and must not contain dashes (`-`).
This allows them to be imported and unittested. If you want an executable to be
accessible without the extension, use a symbolic link or a simple bash wrapper
containing `exec "$0.py" "$@"`.

<a id="s3.16.4-guidelines-derived-from-guidos-recommendations"></a>
<a id="3164-guidelines-derived-from-guidos-recommendations"></a>

<a id="guidelines-derived-from-guidos-recommendations"></a>
#### 3.16.4 Guidelines derived from Guido's Recommendations 

<table rules="all" border="1" summary="Guidelines from Guido's Recommendations"
       cellspacing="2" cellpadding="2">

  <tr>
    <th>Type</th>
    <th>Public</th>
    <th>Internal</th>
  </tr>

  <tr>
    <td>Packages</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Modules</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code></td>
  </tr>

  <tr>
    <td>Classes</td>
    <td><code>CapWords</code></td>
    <td><code>_CapWords</code></td>
  </tr>

  <tr>
    <td>Exceptions</td>
    <td><code>CapWords</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Functions</td>
    <td><code>lower_with_under()</code></td>
    <td><code>_lower_with_under()</code></td>
  </tr>

  <tr>
    <td>Global/Class Constants</td>
    <td><code>CAPS_WITH_UNDER</code></td>
    <td><code>_CAPS_WITH_UNDER</code></td>
  </tr>

  <tr>
    <td>Global/Class Variables</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code></td>
  </tr>

  <tr>
    <td>Instance Variables</td>
    <td><code>lower_with_under</code></td>
    <td><code>_lower_with_under</code> (protected)</td>
  </tr>

  <tr>
    <td>Method Names</td>
    <td><code>lower_with_under()</code></td>
    <td><code>_lower_with_under()</code> (protected)</td>
  </tr>

  <tr>
    <td>Function/Method Parameters</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

  <tr>
    <td>Local Variables</td>
    <td><code>lower_with_under</code></td>
    <td></td>
  </tr>

</table>

While Python supports making things private by using a leading double underscore
`__` (aka. "dunder") prefix on a name, this is discouraged. Prefer the use of a
single underscore. They are easier to type, read, and to access from small
unittests. Lint warnings take care of invalid access to protected members.


<a id="s3.17-main"></a>
<a id="317-main"></a>

<a id="main"></a>
### 3.17 Main 

Even a file meant to be used as an executable should be importable and a mere
import should not have the side effect of executing the program's main
functionality. The main functionality should be in a `main()` function.

In Python, `pydoc` as well as unit tests require modules to be importable. Your
code should always check `if __name__ == '__main__'` before executing your main
program so that the main program is not executed when the module is imported.

```python
def main():
    ...

if __name__ == '__main__':
    main()
```

All code at the top level will be executed when the module is imported. Be
careful not to call functions, create objects, or perform other operations that
should not be executed when the file is being `pydoc`ed.

<a id="s3.18-function-length"></a>
<a id="318-function-length"></a>

<a id="function-length"></a>
### 3.18 Function length 

Prefer small and focused functions.

We recognize that long functions are sometimes appropriate, so no hard limit is
placed on function length. If a function exceeds about 40 lines, think about
whether it can be broken up without harming the structure of the program.

Even if your long function works perfectly now, someone modifying it in a few
months may add new behavior. This could result in bugs that are hard to find.
Keeping your functions short and simple makes it easier for other people to read
and modify your code.

You could find long and complicated functions when working with
some code. Do not be intimidated by modifying existing code: if working with such
a function proves to be difficult, you find that errors are hard to debug, or
you want to use a piece of it in several different contexts, consider breaking
up the function into smaller and more manageable pieces.

<a id="s3.19-type-annotations"></a>
<a id="319-type-annotations"></a>

<a id="type-annotations"></a>
### 3.19 Type Annotations 

<a id="s3.19.1-general"></a>
<a id="3191-general-rules"></a>

<a id="typing-general"></a>
#### 3.19.1 General Rules 

* Familiarize yourself with [PEP-484](https://www.python.org/dev/peps/pep-0484/).
* In methods, only annotate `self`, or `cls` if it is necessary for proper type
  information. e.g., `@classmethod def create(cls: Type[T]) -> T: return cls()`
* If any other variable or a returned type should not be expressed, use `Any`.
* You are not required to annotate all the functions in a module.
  -   At least annotate your public APIs.
  -   Use judgment to get to a good balance between safety and clarity on the
      one hand, and flexibility on the other.
  -   Annotate code that is prone to type-related errors (previous bugs or
      complexity).
  -   Annotate code that is hard to understand.
  -   Annotate code as it becomes stable from a types perspective. In many
      cases, you can annotate all the functions in mature code without losing
      too much flexibility.


<a id="s3.19.2-line-breaking"></a>
<a id="3192-line-breaking"></a>

<a id="typing-line-breaking"></a>
#### 3.19.2 Line Breaking 

Try to follow the existing [indentation](#indentation) rules.

After annotating, many function signatures will become "one parameter per line".

```python
def my_method(self,
              first_var: int,
              second_var: Foo,
              third_var: Optional[Bar]) -> int:
  ...
```

Always prefer breaking between variables, and not for example between variable
names and type annotations. However, if everything fits on the same line,
go for it.

```python
def my_method(self, first_var: int) -> int:
  ...
```

If the combination of the function name, the last parameter, and the return type
is too long, indent by 4 in a new line.

```python
def my_method(
    self, first_var: int) -> Tuple[MyLongType1, MyLongType1]:
  ...
```

When the return type does not fit on the same line as the last parameter, the
preferred way is to indent the parameters by 4 on a new line and align the
closing parenthesis with the def.

```python
Yes:
def my_method(
    self, other_arg: Optional[MyLongType]
) -> Dict[OtherLongType, MyLongType]:
  ...
```

`pylint` allows you to move the closing parenthesis to a new line and align
with the opening one, but this is less readable.

```python
No:
def my_method(self,
              other_arg: Optional[MyLongType]
             ) -> Dict[OtherLongType, MyLongType]:
  ...
```

As in the examples above, prefer not to break types. However, sometimes they are
too long to be on a single line (try to keep sub-types unbroken).

```python
def my_method(
    self,
    first_var: Tuple[List[MyLongType1],
                     List[MyLongType2]],
    second_var: List[Dict[
        MyLongType3, MyLongType4]]) -> None:
  ...
```

If a single name and type is too long, consider using an
[alias](#typing-aliases) for the type. The last resort is to break after the
colon and indent by 4.

```python
Yes:
def my_function(
    long_variable_name:
        long_module_name.LongTypeName,
) -> None:
  ...
```

```python
No:
def my_function(
    long_variable_name: long_module_name.
        LongTypeName,
) -> None:
  ...
```

<a id="s3.19.3-forward-declarations"></a>
<a id="3193-forward-declarations"></a>

<a id="forward-declarations"></a>
#### 3.19.3 Forward Declarations 

If you need to use a class name from the same module that is not yet defined --
for example, if you need the class inside the class declaration, or if you use a
class that is defined below -- use a string for the class name.

```python
class MyClass(object):

  def __init__(self,
               stack: List["MyClass"]) -> None:
```

<a id="s3.19.4-default-values"></a>
<a id="3194-default-values"></a>

<a id="typing-default-values"></a>
#### 3.19.4 Default Values 

As per
[PEP-008](https://www.python.org/dev/peps/pep-0008/#other-recommendations), use
spaces around the `=` _only_ for arguments that have both a type annotation and
a default value.

```python
Yes:
def func(a: int = 0) -> int:
  ...
```
```python
No:
def func(a:int=0) -> int:
  ...
```

<a id="s3.19.5-none-type"></a>
<a id="3195-nonetype"></a>

<a id="none-type"></a>
#### 3.19.5 NoneType 

In the Python type system, `NoneType` is a "first class" type, and for typing
purposes, `None` is an alias for `NoneType`. If an argument can be `None`, it
has to be declared! You can use `Union`, but if there is only one other type,
use `Optional`.

Use explicit `Optional` instead of implicit `Optional`. Earlier versions of PEP
484 allowed `a: Text = None` to be interpretted as `a: Optional[Text] = None`,
but that is no longer the preferred behavior.

```python
Yes:
def func(a: Optional[Text], b: Optional[Text] = None) -> Text:
  ...
def multiple_nullable_union(a: Union[None, Text, int]) -> Text
  ...
```

```python
No:
def nullable_union(a: Union[None, Text]) -> Text:
  ...
def implicit_optional(a: Text = None) -> Text:
  ...
```

<a id="s3.19.6-aliases"></a>
<a id="3196-type-aliases"></a>
<a id="typing-aliases"></a>

<a id="type-aliases"></a>
#### 3.19.6 Type Aliases 

You can declare aliases of complex types. The name of an alias should be
CapWorded. If the alias is used only in this module, it should be
\_Private.

For example, if the name of the module together with the name of the type is too
long:

```python
_ShortName = module_with_long_name.TypeWithLongName
ComplexMap = Mapping[Text, List[Tuple[int, int]]]
```

Other examples are complex nested types and multiple return variables from a
function (as a tuple).

<a id="s3.19.7-ignore"></a>
<a id="3197-ignoring-types"></a>

<a id="typing-ignore"></a>
#### 3.19.7 Ignoring Types 

You can disable type checking on a line with the special comment
`# type: ignore`.

`pytype` has a disable option for specific errors (similar to lint):

```python
# pytype: disable=attribute-error
```

<a id="s3.19.8-comments"></a>
<a id="3198-typing-internal-variables"></a>

<a id="typing-variables"></a>
#### 3.19.8 Typing Variables 

If an internal variable has a type that is hard or impossible to infer, you can
specify its type in a couple ways.

<a id="type-comments"></a>
[*Type Comments:*](#type-comments)
:   Use a `# type:` comment on the end of the line

```python
a = SomeUndecoratedFunction()  # type: Foo
```

[*Annotated Assignments*](#annotated-assignments)
:   Use a colon and type between the variable name and value, as with function
    arguments.

```python
a: Foo = SomeUndecoratedFunction()
```

<a id="s3.19.9-tuples"></a>
<a id="3199-tuples-vs-lists"></a>

<a id="typing-tuples"></a>
#### 3.19.9 Tuples vs Lists 

Unlike Lists, which can only have a single type, Tuples can have either a single
repeated type or a set number of elements with different types. The latter is
commonly used as return type from a function.

```python
a = [1, 2, 3]  # type: List[int]
b = (1, 2, 3)  # type: Tuple[int, ...]
c = (1, "2", 3.5)  # type: Tuple[int, Text, float]
```

<a id="s3.19.10-type-var"></a>
<a id="31910-typevar"></a>
<a id="typing-type-var"></a>

<a id="typevars"></a>
#### 3.19.10 TypeVars 

The Python type system has
[generics](https://www.python.org/dev/peps/pep-0484/#generics). The factory
function `TypeVar` is a common way to use them.

Example:

```python
from typing import List, TypeVar
T = TypeVar("T")
...
def next(l: List[T]) -> T:
  return l.pop()
```

A TypeVar can be constrained:

```python
AddableType = TypeVar("AddableType", int, float, Text)
def add(a: AddableType, b: AddableType) -> AddableType:
  return a + b
```

A common predefined type variable in the `typing` module is `AnyStr`. Use it for
multiple annotations that can be `bytes` or `unicode` and must all be the same
type.

```python
from typing import AnyStr
def check_length(x: AnyStr) -> AnyStr:
  if len(x) <= 42:
    return x
  raise ValueError()
```

<a id="s3.19.11-strings"></a>
<a id="31911-string-types"></a>

<a id="typing-strings"></a>
#### 3.19.11 String types 

The proper type for annotating strings depends on what versions of Python the
code is intended for.

For Python 3 only code, prefer to use `str`. `Text` is also acceptable. Be
consistent in using one or the other.

For Python 2 compatible code, use `Text`. In some rare cases, `str` may make
sense; typically to aid compatibility when the return types aren't the same
between the two Python versions. Avoid using `unicode`: it doesn't exist in
Python 3.

The reason this discrepancy exists is because `str` means different things
depending on the Python version.

```python
No:
def py2_code(x: str) -> unicode:
  ...
```

For code that deals with binary data, use `bytes`.

```python
def deals_with_binary_data(x: bytes) -> bytes:
  ...
```

For Python 2 compatible code that processes text data (`str` or `unicode` in
Python 2, `str` in Python 3), use `Text`. For Python 3 only code that process
text data, prefer `str`.

```python
from typing import Text
...
def py2_compatible(x: Text) -> Text:
  ...
def py3_only(x: str) -> str:
  ...
```

If the type can be either bytes or text, use `Union`, with the appropriate text
type.

```python
from typing import Text, Union
...
def py2_compatible(x: Union[bytes, Text]) -> Union[bytes, Text]:
  ...
def py3_only(x: Union[bytes, str]) -> Union[bytes, str]:
  ...
```

If all the string types of a function are always the same, for example if the
return type is the same as the argument type in the code above, use
[AnyStr](#typing-type-var).

Writing it like this will simplify the process of porting the code to Python 3.

<a id="s3.19.12-imports"></a>
<a id="31912-imports-for-typing"></a>

<a id="typing-imports"></a>
#### 3.19.12 Imports For Typing 

For classes from the `typing` module, always import the class itself. You are
explicitly allowed to import multiple specific classes on one line from the
`typing` module. Ex:

```python
from typing import Any, Dict, Optional
```

Given that this way of importing from `typing` adds items to the local
namespace, any names in `typing` should be treated similarly to keywords, and
not be defined in your Python code, typed or not. If there is a collision
between a type and an existing name in a module, import it using
`import x as y`.

```python
from typing import Any as AnyType
```

<a id="s3.19.13-conditional-imports"></a>
<a id="31913-conditional-imports"></a>

<a id="typing-conditional-imports"></a>
#### 3.19.13 Conditional Imports 

Use conditional imports only in exceptional cases where the additional imports
needed for type checking must be avoided at runtime. This pattern is
discouraged; alternatives such as refactoring the code to allow top level
imports should be preferred.

Imports that are needed only for type annotations can be placed within an
`if TYPE_CHECKING:` block.

-   Conditionally imported types need to be referenced as strings, to be forward
    compatible with Python 3.6 where the annotation expressions are actually
    evaluated.
-   Only entities that are used solely for typing should be defined here; this
    includes aliases. Otherwise it will be a runtime error, as the module will
    not be imported at runtime.
-   The block should be right after all the normal imports.
-   There should be no empty lines in the typing imports list.
-   Sort this list as if it were a regular imports list.
```python
import typing
if typing.TYPE_CHECKING:
  import sketch
def f(x: "sketch.Sketch"): ...
```

<a id="s3.19.14-circular-deps"></a>
<a id="31914-circular-dependencies"></a>

<a id="typing-circular-deps"></a>
#### 3.19.14 Circular Dependencies 

Circular dependencies that are caused by typing are code smells. Such code is a
good candidate for refactoring. Although technically it is possible to keep
circular dependencies, the [build system](#typing-build-deps) will not let you
do so because each module has to depend on the other.

Replace modules that create circular dependency imports with `Any`. Set an
[alias](#typing-aliases) with a meaningful name, and use the real type name from
this module (any attribute of Any is Any). Alias definitions should be separated
from the last import by one line.

```python
from typing import Any

some_mod = Any  # some_mod.py imports this module.
...

def my_method(self, var: some_mod.SomeType) -> None:
  ...
```

<a id="typing-generics"></a>
<a id="s3.19.15-generics"></a>
<a id="31915-generics"></a>

<a id="generics"></a>
#### 3.19.15 Generics 

When annotating, prefer to specify type parameters for generic types; otherwise,
[the generics' parameters will be assumed to be `Any`](https://www.python.org/dev/peps/pep-0484/#the-any-type).

```python
def get_names(employee_ids: List[int]) -> Dict[int, Any]:
  ...
```

```python
# These are both interpreted as get_names(employee_ids: List[Any]) -> Dict[Any, Any]
def get_names(employee_ids: list) -> Dict:
  ...

def get_names(employee_ids: List) -> Dict:
  ...
```

If the best type parameter for a generic is `Any`, make it explicit, but
remember that in many cases [`TypeVar`](#typing-type-var) might be more
appropriate:

```python
def get_names(employee_ids: List[Any]) -> Dict[Any, Text]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```

```python
T = TypeVar('T')
def get_names(employee_ids: List[T]) -> Dict[T, Text]:
  """Returns a mapping from employee ID to employee name for given IDs."""
```


<a id="4-parting-words"></a>

<a id="consistency"></a>
## 4 Parting Words 

*BE CONSISTENT*.

If you're editing code, take a few minutes to look at the code around you and
determine its style. If they use spaces around all their arithmetic operators,
you should too. If their comments have little boxes of hash marks around them,
make your comments have little boxes of hash marks around them too.

The point of having style guidelines is to have a common vocabulary of coding so
people can concentrate on what you're saying rather than on how you're saying
it. We present global style rules here so people know the vocabulary, but local
style is also important. If code you add to a file looks drastically different
from the existing code around it, it throws readers out of their rhythm when
they go to read it. Avoid this.


