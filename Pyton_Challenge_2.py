""" Create  a  function  that  calculates  the  power  of  a  number.
Then  write  a  unit  test  to  check  the  correctness  of  the
function.
"""


def exponent(num, exp):
    result = 1
    for i in range(exp):
        result *= num
    return result


print(pow(7, 5))
print(exponent(7, 5))

