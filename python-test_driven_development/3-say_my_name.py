#!/usr/bin/python3
def say_my_name(first_name, last_name=''):
    err_msg = {}
    err_msg["FirstNotStr"] = "first_name must be a string"
    err_msg["LastNotStr"] = "last_name must be a string"

    if type(first_name) != str:
        raise TypeError(err_msg["FirstNotStr"])
    if type(last_name) != str:
        raise TypeError(err_msg["LastNotStr"])

    print("My name is {}".format(first_name), end='')
    if len(last_name) == 0:
        print()
    else:
        print(" {}".format(last_name))
