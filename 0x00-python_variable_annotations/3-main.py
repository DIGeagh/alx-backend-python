#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))  # True
print(to_str.__annotations__)  # {'n': <class 'float'>, 'return': <class 'str'>}
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
