""" Create  a  function  that  converts  any  string  value  to  upper
case,  Then  write  a  unit  test  that  checks  the  function's
correctness.
"""


def to_upper(string):
    upper_c = ""
    for i in string:
        if i.islower():
            upper_c += i.upper()
    print(upper_c)


to_upper("happiness")
