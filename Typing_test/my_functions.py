#!/usr/bin/python3

# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
from time import time


# ------------------------
##   DATA STRUCTURES   ##
# ------------------------


# ------------------------
## FUNCTION DEFINITION ##
# ------------------------
def tic():
    """
    Functions used to return the numbers of seconds passed since epoch to use with function toc() afterwards.
    Like tic toc matlab functions.
    :return: a float.
    """

    # Get the number os seconds passed since epoch
    start_time = time()

    return start_time


def toc(start_time):
    """
    Function used to return the elapsed time since function tic() was used. tic() and toc() works together.
    :param start_time: number of seconds passed since epoch given by tic() function. Datatype: float
    :return: a float.
    """

    # Get the number of seconds passed since epoch and subtract from tic(). This is the elapsed time from tic to toc.
    end_time = time()
    elapsed_time = end_time - start_time

    return elapsed_time
