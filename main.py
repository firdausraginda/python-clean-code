import os
import typing

with open("/path/to/some/file/you/want/to/read") as file_1, open(
    "/path/to/some/file/being/written", "w"
) as file_2:
    file_2.write(file_1.read())


def ini_function_panjang(
    argument_1, argument_2, argument_3, argument_4, argument_5, argument_6="def_val"
):
    pass


class Foo:  # this is inlince comment
    def __init__(self) -> None:
        pass

    def foo(self):
        pass


def bar():
    pass


my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
]
result = some_function_that_takes_arguments(  # this is a comment
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
)
