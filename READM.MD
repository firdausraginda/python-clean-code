# Table of Contents

1. [S.O.L.I.D. Principles](https://github.com/firdausraginda/python-clean-code/blob/main/READM.MD#solid-principles)
2. [Clean Code in Writting a Function](https://github.com/firdausraginda/python-clean-code/blob/main/READM.MD#clean-code-in-writting-a-function)
3. [Dataclasses](https://github.com/firdausraginda/python-clean-code/blob/main/READM.MD#dataclasses)
4. [PEP 8 - Style Guide](https://github.com/firdausraginda/python-clean-code/blob/main/READM.MD#pep-8---style-guide)

---

# S.O.L.I.D. Principles

reference:
* https://www.youtube.com/watch?v=pTB30aXS77U
* https://towardsdatascience.com/solid-coding-in-python-1281392a6a94
* https://www.pythontutorial.net/python-oop/python-dependency-inversion-principle/

## Single Responsibility Principle
Every component of our code (in general a class, but also a function) should have one and only one responsibility. As a consequence of that, there should be only a reason to change it.

## Open–Closed Principle
We should not need to modify the code that already written to accommodate new functionality, but simply add what we need now. Should use abstract base class (ABC) for this.

## Liskov Substitution Principle
Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it. In other words, what we want is to have the objects of our subclasses behaving the same way as the objects of our superclass.

## Interface Segregation Principle
Many client-specific interfaces are better than one general-purpose interface.

## Dependency Inversion Principle
High-level modules should not depend on low-level modules. Both should depend on abstractions.

---

# Clean Code in Writting a Function

reference: 
* https://www.youtube.com/watch?v=yatgY4NpZXE

## Seperate Commands from Queries
Directly return the result of a function if possible
```
def validate_card(customer: Customer) -> bool:
    return (
        luhn_checksum(customer.cc_number)
        and datetime(customer.cc_exp_year, customer.cc_exp_month, 1) > datetime.now()
    )
```

## Only Accept Parameters That Needed Inside The Function
If a function only requires 3 values with string type, pass only those 3 values in string type.
hint: specify `*` in function parameter to force specify the keyword argument when call a function.
```
def validate_card(*, number: str, exp_month: int, exp_year: int) -> bool:
    return (
        luhn_checksum(number)
        and datetime(exp_year, exp_month, 1) > datetime.now()
    )
```

## Keep The Number of Parameters Minimal
If a function requires to many parameters, create 1 class that inherit **Protocol** as superclass.
```
from typing import Protocol

class cardInfo(Protocol):
    @property
    def number(self) -> str:
        ...
    
    @property
    def exp_month(self) -> int:
        ...

    @property
    def exp_year(self) -> int:
        ...

def validate_card(card: CardInfo) -> bool:
    return (
        luhn_checksum(card.number)
        and datetime(card.exp_year, card.exp_month, 1) > datetime.now()
    )

def main() -> None:
    card = Card(number="1249190007575069", exp_month=1, exp_year=2024) 
    card.valid = validate_card(card)
```


## Don't Create and Use an Object in The Same Place
Create object in a function, and use it in different function

## Don't Use Flag Arguments
Flag argument means there are only 2 possibilities: true or false. Better to split it to 2 different functions.

## Function & Parameter Naming Tips
Function name should be action, it should be a 'verb'. And argument should be 'nouns'.
Example: greeting(name)

## Group Side Effects & Use Pure Functions

### Function with side effect vs pure function
* function with side effects: when function/method relies on or modify something on the outside of that function. It makes code harder to maintain & to test bc we can't isolate the function properly.
  * example: printing something, read from a file, write to a file, interact with database, interact with other services
* pure function: if function doesn't have side effect, and the returned value only determined by its input values. This easier to maintain & to test.

### Solution
The solution is to group code inside all function with side effect to one place. And turn other function to pure functions.

### Example on Class
#### before
```
from datetime import datetime
from typing import List


class Greeting:
    def __init__(self) -> None:
        current_time = datetime.now()
        if current_time.hour < 12:
            self.greeting_intro = "Good morning"
        elif 12 <= current_time.hour < 12:
            self.greeting_intro = "Good afternoon"
        else:
            self.greeting_intro = "Good evening"

    def greet(self, name: str) -> None:
        print(f"{self.greeting_intro}, {name}.")

    def greet_list(self, names: List[str]) -> None:
        for name in names:
            self.greet(name)


def main() -> None:
    name = input("Enter your name: ")

    greeting = Greeting()
    greeting.greet(name)


if __name__ == "__main__":
    main()
```

#### after
```
from datetime import datetime
from typing import List


class Greeting:
    def __init__(self, greeting_intro: str) -> None:
        self.greeting_intro = greeting_intro

    def greet(self, name: str) -> None:
        return f"{self.greeting_intro}, {name}."

    def greet_list(self, names: List[str]) -> List[str]:
        greetings: List[str] = []
        for name in names:
            greetings.append(self.greet(name))

        return greetings


def main() -> None:
    current_time = datetime.now()
    if current_time.hour < 12:
        greeting_intro = "Good morning"
    elif 12 <= current_time.hour < 12:
        greeting_intro = "Good afternoon"
    else:
        greeting_intro = "Good evening"

    name = input("Enter your name: ")

    greeting = Greeting(greeting_intro)
    print(greeting.greet(name))
    print("\n".join(greeting.greet_list(["John", "Jane", "Joe"])))


if __name__ == "__main__":
    main()
```

### Example on Function

#### after
```
from datetime import datetime
from typing import List


def greet(name: str, greeting_intro: str) -> str:
    return f"{greeting_intro}, {name}."


def greet_list(names: List[str], greeting_intro: str) -> List[str]:
    return [greet(name, greeting_intro) for name in names]


def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good morning"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def read_name() -> str:
    return input("Enter your name: ")


def main():
    print(greet(read_name(), read_greeting()))
    print(greet_list(["John", "Jane", "Joe"], read_greeting()))


if __name__ == "__main__":
    main()
```

---

# Dataclasses

reference:
* https://www.youtube.com/watch?v=vRVVyl9uaZc&list=PLeGc_lalTbVHuDY-nbYLCUkIByRaAyUzV&index=7

## Data-Driven Classes
Dataclasses provide functionality to print, compare, & order data that easier to use than regular function. Those are mostly used for analytical purposes.

## Regular Class vs Dataclasses

#### regular classes
```
class Person:
    def __init__(self, name, job, age) -> None:
        self.name = name
        self.job = job
        self.age = age


person1 = Person("geralt", "UX designer", 27)
person2 = Person("wanda", "UI engineer", 25)
```

#### dataclasses
```
from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int = 100

    def __post_init__(self):
        self.sort_index = self.age


person1 = Person("geralt", "UX designer", 27)
person2 = Person("wanda", "UI engineer")
```

  * `init=False`: don't need to specify value of `sort_index` when create object
  * `repr=False`: `sort_index` will not shown when print the object

---

# PEP 8 - Style Guide

reference: 
* https://peps.python.org/pep-0008/

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

### If-else statement with multiple conditions
```
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

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

## When to Use Trailing Commas

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

## Comments

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

## Other Recommendations

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

### When combining an argument annotation with a default value, however, do use spaces around the = sign
```
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```

### Compound statements (multiple statements on the same line) are generally discouraged
```
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
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