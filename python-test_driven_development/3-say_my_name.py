#!/usr/bin/python3
"""
Defines a name printing function.
"""


def say_my_name(*args, **kwargs):
    """
    Prints My name is <first name> <last name>.
    Raises TypeError if first_name or last_name is not a string,
    or if required arguments are missing.
    """
    # Extract arguments handling potential explicit keywords or positional args
    first_name = kwargs.get('first_name')
    last_name = kwargs.get('last_name', "")

    if len(args) > 0:
        first_name = args[0]
    if len(args) > 1:
        last_name = args[1]

    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
