# S.O.L.I.D. Principles


# PEP 8 - Style Guide
---
reference: https://peps.python.org/pep-0008/

## Indentation

### Aligned with opening delimiter
```
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

### Hanging indents should add a level
```
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

### Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest
```
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

### No extra indentation
```
if (this_is_one_thing and
    that_is_another_thing):
    do_something()
```

### Add some extra indentation on the conditional continuation line
```
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

### The closing brace/bracket/parenthesis
```
my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

### Math operator as function arguments
```
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

## Imports

```
import os
import sys
from subprocess import Popen, PIPE
```

## Whitespace in Expressions and Statements

### Immediately inside parentheses, brackets or braces
```
spam(ham[1], {eggs: 2})
```

### Between a trailing comma and a following close parenthesis
```
foo = (0,)
```

### Immediately before a comma, semicolon, or colon
```
if x == 4: print(x, y); x, y = y, x
```

### Immediately before the open parenthesis that starts the argument list of a function call
```
spam(1)
```

### Immediately before the open parenthesis that starts an indexing or slicing
```
dct['key'] = lst[index]
```

### More than one space around an assignment (or other) operator to align it with another
```
x = 1
y = 2
long_variable = 3
```

### Math operator when define a variable
```
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

### Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present
```
def munge(input: AnyStr): ...
def munge() -> PosInt: ...
```

### Don’t use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter
```
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

### When combining an argument annotation with a default value, however, do use spaces around the = sign:
```
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```

### Compound statements (multiple statements on the same line) are generally discouraged:
```
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```

### Trailing commas
```
FILES_1 = ('setup.cfg',)
FILES_2 = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
```

### Inline comment
```
x = x + 1  # Increment x
```

### Documentation string
```
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```

### Try and except
```
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
```

### Consistent on return null
```
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
```

### Checking data type
```
if isinstance(obj, int):
```