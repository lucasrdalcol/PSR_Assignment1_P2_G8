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

    global start_time
    start_time = time()


def toc():
    """
    Function used to print the elapsed time since function tic() was used. tic() and toc() works together.
    :return: a float.
    """

    # Get the number os seconds passed since epoch and subtract from tic(). This is the elapsed time from tic to toc.

    # Check if start_time is inside global variables
    if 'start_time' in globals():
        last_time = time()
        elapsed_time = last_time - start_time
        print('Elapsed time: ' + str(elapsed_time) + ' seconds.')
    else:
        print('Error: start time from tic() not set')