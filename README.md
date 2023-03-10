# Table of Contents

1. [S.O.L.I.D. Principles](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#solid-principles) 
   * [Single Responsibility Principle](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#single-responsibility-principle)
   * [Open–Closed Principle](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#openclosed-principle)
   * [Liskov Substitution Principle](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#liskov-substitution-principle)
   * [Interface Segregation Principle](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#interface-segregation-principle)
   * [Dependency Inversion Principle](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#dependency-inversion-principle)
2. [Abstract Base Class (ABC) vs Protocol](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#abstract-base-class-abc-vs-protocol)
3. [Clean Code in Writting a Function](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#clean-code-in-writting-a-function)
   * [Seperate Commands from Queries](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#seperate-commands-from-queries)
   * [Only Accept Parameters That Needed Inside The Function](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#only-accept-parameters-that-needed-inside-the-function)
   * [Keep The Number of Parameters Minimal](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#keep-the-number-of-parameters-minimal)
   * [Don't Create and Use an Object in The Same Place](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#dont-create-and-use-an-object-in-the-same-place)
   * [Don't Use Flag Arguments](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#dont-use-flag-arguments)
   * [Function & Parameter Naming Tips](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#function--parameter-naming-tips)
   * [Group Side Effects & Use Pure Functions](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#group-side-effects--use-pure-functions)
   * [Function as First-Class Citizens](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#function-as-first-class-citizens)
4. [Dataclasses](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#dataclasses)
   * [Data-Driven Classes](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#data-driven-classes)
   * [Regular Class vs Dataclasses](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#regular-class-vs-dataclasses)
5. [Try and Except](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#try-and-except)
   * [Low-Level & High-Level Error Handling](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#low-level--high-level-error-handling)
   * [Using Context-Manager](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#using-context-manager)
6. [PEP 8 - Style Guide](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#pep-8---style-guide)
   * [Indentation](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#indentation)
   * [Imports](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#imports)
   * [Whitespace in Expressions and Statements](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#whitespace-in-expressions-and-statements)
   * [When to Use Trailing Commas](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#when-to-use-trailing-commas)
   * [Comments](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#comments)
   * [Other Recommendations](https://github.com/firdausraginda/python-clean-code/blob/main/README.md#other-recommendations)

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

# Abstract Base Class (ABC) vs Protocol

reference:
* https://www.youtube.com/watch?v=xvb5hGLoK0A&list=PLeGc_lalTbVHuDY-nbYLCUkIByRaAyUzV&index=5&t=1156s

Both ABC & protocol, act as abstraction class, that can have subclasses.

The different is only on the subclass:
* ABC: the subclass must have exact same methods, even if some methods are not used in the subclass.
* protocol: the subclass doesn't have to have exact same methods. If the subclass doesn't need it, then don't need to specify it.

#### example using ABC
```py
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass


class iphone(Device):
    def connect(self) -> None:
        return "iphone connecting..."

    def disconnect(self) -> None:
        return "iphone disconnecting..."


iphone_1 = iphone()
print(iphone_1.connect())
print(iphone_1.disconnect())
```

#### example using protocol
```py
from typing import Protocol


class Device(Protocol):
    def connect(self) -> None:
        ...

    def disconnect(self) -> None:
        ...


class iphone(Device):
    def connect(self) -> None:
        return "iphone connecting..."


iphone_1 = iphone()
print(iphone_1.connect())
```

---

# Clean Code in Writting a Function

reference: 
* https://www.youtube.com/watch?v=yatgY4NpZXE

## Seperate Commands from Queries
Directly return the result of a function if possible
```py
def validate_card(customer: Customer) -> bool:
    return (
        luhn_checksum(customer.cc_number)
        and datetime(customer.cc_exp_year, customer.cc_exp_month, 1) > datetime.now()
    )
```

## Only Accept Parameters That Needed Inside The Function
If a function only requires 3 values with string type, pass only those 3 values in string type. Specify `*` in function parameter to force keyword argument specified when call the function.
```py
def validate_card(*, number: str, exp_month: int, exp_year: int) -> bool:
    return (
        luhn_checksum(number)
        and datetime(exp_year, exp_month, 1) > datetime.now()
    )
```

## Keep The Number of Parameters Minimal
If a function requires to many parameters, create 1 class that inherit **Protocol** as superclass.
```py
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
  * example of side effects: printing something, read from a file, write to a file, interact with database, interact with other services.
* pure function: if function doesn't have side effect, and the returned value only determined by its input values. This easier to maintain & to test.

The idea is to put code inside all function with side effect to one place. And turn other function to pure functions.

### Example on Class

#### before
```py
from datetime import datetime
from typing import List


class Greeting:
    def __init__(self) -> None:
        # ------ relies on something outside the function that create side effects ------
        current_time = datetime.now()
        if current_time.hour < 12:
            self.greeting_intro = "Good morning"
        elif 12 <= current_time.hour < 12:
            self.greeting_intro = "Good afternoon"
        else:
            self.greeting_intro = "Good evening"
        # ------ relies on something outside the function that create side effects ------

    def greet(self, name: str) -> None:
        # ------ create side effects ------
        print(f"{self.greeting_intro}, {name}.")
        # ------ create side effects ------

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
```py
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
```py
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

## Function as First-Class Citizens

The idea is to supply a function as parameter to a function. 

The advantage of doing this is, after pass it to the designated function, we can set condition when it should be called. So it will not be called all the time.

#### example use callable
```py
from datetime import datetime
from typing import List, Callable

# callable that doesn't take any arguments but return string
GreetingReader = Callable[[], str]


def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name.lower() == "agi":
        return "bugger off!"

    return f"{greeting_reader()}, {name}."  # function greeting_reader() only called if name is not "agi"


def greet_list(names: List[str], greeting_reader: GreetingReader) -> List[str]:
    return [greet(name, greeting_reader) for name in names]


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


def main() -> None:
    print(greet(read_name(), read_greeting))
    print(greet_list(["John", "Jane", "Joe"], read_greeting))


if __name__ == "__main__":
    main()
```

#### example use callable & partial
partial lib is to predefined value of function argument, so we don't need to specify that argument again whenever call the function.

```py
from datetime import datetime
from typing import List, Callable
from functools import partial

GreetingReader = Callable[[], str]
GreetingFunction = Callable[[str], str]


def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name.lower() == "agi":
        return "bugger off!"

    return f"{greeting_reader()}, {name}."


def greet_list(names: List[str], greeting_fn: GreetingFunction) -> List[str]:
    return [greeting_fn(name) for name in names]


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


def main() -> None:
    greeting_fn = partial(greet, greeting_reader=read_greeting)
    print(greeting_fn(read_name()))
    print(greet_list(["John", "Jane", "Joe"], greeting_fn))


if __name__ == "__main__":
    main()
```

---

# Dataclasses

reference:
* https://www.youtube.com/watch?v=vRVVyl9uaZc&list=PLeGc_lalTbVHuDY-nbYLCUkIByRaAyUzV&index=7

Dataclasses is a data-driven classes, meaning it provides functionality to print, compare, & order data that easier to use than regular function. Those are mostly used for analytical purposes.

## Regular Class vs Dataclasses

#### regular classes
```py
class Person:
    def __init__(self, name, job, age) -> None:
        self.name = name
        self.job = job
        self.age = age


person1 = Person("geralt", "UX designer", 27)
person2 = Person("wanda", "UI engineer", 25)
```

#### dataclasses
```py
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

# Try and Except

For flask API case, in endpoint level we want to have high level error, while in usecase / repo level we want to have low level error.

It is better to catch specific error in `except` statement instead of general error.

## Low-Level & High-Level Error Handling

### repo / usecase level
```py

# ------ custom error handler ------
class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass
# ------ custom error handler ------

def fetch_blog(id: str):
    try:
        # connect to the database
        con = sqlite3.connect('application.db')
        cur = con.cursor()

        # execute the query and fetch the data
        cur.execute(f"SELECT * FROM blogs where id=?", [id])
        result = cur.fetchone()

        # return the result or raise an error
        if result is None:
            raise NotFoundError(f'Unable to find blog with id {id}.')
        
        data = blog_lst_to_json(result)
        if not data['public']:
            raise NotAuthorizedError(f'You are not allowed to access blog with id {id}.')
        return data
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundError(f'Unable to find blog with id {id}.')
    finally:
        print("Closing the database")
        # close the database
        con.close()
```

### endpoint level
```py
from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog, NotFoundError, NotAuthorizedError

app = Flask(__name__)

@app.route('/blogs/<id>')
def get_blog(id):
    try:
        return jsonify(fetch_blog(id))
    except NotFoundError:
        abort(404, description="Resource not found")
    except NotAuthorizedError:
        abort(403, description="Access denied")
```

## Using Context-Manager
Other alternative is we can use context-manager.

### repo / usecase level
```py
class SQLite():
    def __init__(self, file='application.db'):
        self.file=file
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        print("Closing the connection")
        self.conn.close()

class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass

def fetch_blog(id: str):
    try:
        with SQLite('application.db') as cur:

            # execute the query and fetch the data
            cur.execute(f"SELECT * FROM blogs where id=?", [id])
            result = cur.fetchone()

            # return the result or raise an error
            if result is None:
                raise NotFoundError(f'Unable to find blog with id {id}.')
        
            data = blog_lst_to_json(result)
            if not data['public']:
                raise NotAuthorizedError(f'You are not allowed to access blog with id {id}.')
            return data
    except sqlite3.OperationalError:
        raise NotFoundError(f'Unable to find blog with id {id}.')
```

### endpoint level
in endpoint level same as above

---

# PEP 8 - Style Guide

reference: 
* https://peps.python.org/pep-0008/

## Indentation

### Aligned with opening delimiter
```py
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

### Hanging indents should add a level
```py
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

### Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest
```py
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

### If-else statement with multiple conditions
```py
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

### The closing brace/bracket/parenthesis
```py
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
```py
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

## Imports

```py
import os
import sys
from subprocess import Popen, PIPE
```

## Whitespace in Expressions and Statements

### Immediately inside parentheses, brackets or braces
```py
spam(ham[1], {eggs: 2})
```

### Between a trailing comma and a following close parenthesis
```py
foo = (0,)
```

### Immediately before a comma, semicolon, or colon
```py
if x == 4: print(x, y); x, y = y, x
```

### Immediately before the open parenthesis that starts the argument list of a function call
```py
spam(1)
```

### Immediately before the open parenthesis that starts an indexing or slicing
```py
dct['key'] = lst[index]
```

### More than one space around an assignment (or other) operator to align it with another
```py
x = 1
y = 2
long_variable = 3
```

## When to Use Trailing Commas

### Trailing commas
```py
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
```py
x = x + 1  # Increment x
```

### Documentation string
```py
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```

## Other Recommendations

### Math operator when define a variable
```py
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

### Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present
```py
def munge(input: AnyStr): ...
def munge() -> PosInt: ...
```

### Don’t use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter
```py
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

### When combining an argument annotation with a default value, however, do use spaces around the = sign
```py
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```

### Compound statements (multiple statements on the same line) are generally discouraged
```py
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```

### Try and except
```py
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
```

### Consistent on return null
```py
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
```py
if isinstance(obj, int):
```
