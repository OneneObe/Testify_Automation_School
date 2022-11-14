""" Writing  a  well-documented  code  creates  a  function  that
calculates simple interest.
"""


def simple_interest(p, t, r):
    """ p = Principal
        t = Time
        r = Rate"""
    SI = (p * t * r) / 100
    print(SI)


simple_interest(10, 6, 2)
