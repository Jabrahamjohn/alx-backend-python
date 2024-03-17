#!/usr/bin/env python3
"""this initializes a script"""


def vars(a:int, pi:float,i_understand_annotations:bool, school:str) -> tuple:
    """this function vars annotates variables as specified
    args:
    a: integer value
    pi: float value
    i_understand annotations: boolean value
    school: string value
    Returns:
    the variables
    """
    return int(a),float(pi),bool(i_understand_annotations),str(school)
