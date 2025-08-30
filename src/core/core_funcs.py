from typing import List


def ext_list(inp: List, a: int | float, b: int | float) -> List:
    """Return input list extended about added a+b"""
    c = a + b
    inp.append(c)
    return c
