#!/usr/bin/python3

# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
from collections import namedtuple
from colorama import Fore
from numpy.random import randint
import time
from my_classes import *
import readchar
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import Terminal256Formatter
from pprint import pformat

# ------------------------
##   DATA STRUCTURES   ##
# ------------------------
Input = namedtuple('Input', ['requested', 'received', 'duration'])


# ------------------------
## FUNCTION DEFINITION ##
# ------------------------
def tic():
    """
    Functions used to return the numbers of seconds passed since epoch to use with function toc() afterwards.
    Like tic toc matlab functions.
    :return start_time: a float.
    """

    # Get the number os seconds passed since epoch
    start_time = time.time()

    return start_time


def toc(start_time):
    """
    Function used to return the elapsed time since function tic() was used. tic() and toc() works together.
    :param start_time: number of seconds passed since epoch given by tic() function. Datatype: float
    :return elapsed_time: a float.
    """

    # Get the number of seconds passed since epoch and subtract from tic(). This is the elapsed time from tic to toc.
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time


def typing_test(use_time_mode, max_value):
    """
    Function to compute the typing test.
    :param use_time_mode: Use time mode or input mode
    :param max_value: maximum value of seconds within time mode or maximum value of inputs within input mode
    :return inputs: list of namedtuples
    """

    # Initialize list of inputs and counter of number of inputs
    inputs = []
    number_inputs = 0

    print(Fore.BLUE + '\nPress space bar to abort the test.\n' + Fore.RESET)

    # Use time mode or use input mode
    if use_time_mode:
        try:  # Stop the program immediately when time runs out
            with Timeout(max_value):  # Call class Timeout with the max value
                while True:
                    # Generate random low case letter
                    low_case = randint(97, 122)
                    print('Type letter ' + Fore.BLUE + chr(low_case) + Fore.RESET)

                    # Get pressed key from keyboard and time of response
                    type_time_start = tic()
                    pressed_key = readchar.readkey()
                    type_elapsed_time = toc(type_time_start)

                    # Analyse pressed key to see if it's a space, to stop the code.
                    if pressed_key == str(' '):
                        print('\nYou pressed the space bar, test aborted.')
                        exit(0)

                    # Create tuple with requested and received key with its durations and append to a list for the
                    # dict later on.
                    input_namedtuple = Input(requested=chr(low_case), received=pressed_key,
                                             duration=round(type_elapsed_time, 2))
                    inputs.append(input_namedtuple)

                    # Check the pressed key with the random low case letter
                    if pressed_key == chr(low_case):
                        print('You typed letter ' + Fore.GREEN + pressed_key + Fore.RESET)
                    else:
                        print('You typed letter ' + Fore.RED + pressed_key + Fore.RESET)

        except Timeout.Timeout:
            pass

    else:
        while number_inputs < max_value:
            # Generate random low case letter
            low_case = randint(97, 122)
            print('Type letter ' + Fore.BLUE + chr(low_case) + Fore.RESET)

            # Get pressed key from keyboard and time of response
            type_time_start = tic()
            pressed_key = readchar.readkey()
            type_elapsed_time = toc(type_time_start)

            # Analyse pressed key to see if it's a space, to stop the code.
            if pressed_key == str(' '):
                print(Fore.RED + '\n----ATTENTION----' + Fore.RESET)
                print('You pressed the space bar, test aborted.\n')
                exit(0)

            # Create tuple with requested and received key with its durations and append to a list for the dict later
            # on.
            input_namedtuple = Input(requested=chr(low_case), received=pressed_key,
                                     duration=round(type_elapsed_time, 2))
            inputs.append(input_namedtuple)

            # Check the pressed key with the random low case letter
            if pressed_key == chr(low_case):
                print('You typed letter ' + Fore.GREEN + pressed_key + Fore.RESET)
            else:
                print('You typed letter ' + Fore.RED + pressed_key + Fore.RESET)

            number_inputs += 1

    return inputs


def pprint_color(obj):
    """
    Function that return the pretty print with colors.
    :param obj: the string that should be printed.
    """
    print(highlight(pformat(obj), PythonLexer(), Terminal256Formatter()))
