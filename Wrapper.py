import numpy as np
import pandas as pd

def wrap1(num):
    def inner():
        b = num()
        multi= b*10
        return multi
    return inner

def wrap(num):
    def inner():
        a= num()
        add= a + 20
        return add
    return inner

@wrap
@wrap1
def num():
    return 10

print(num())