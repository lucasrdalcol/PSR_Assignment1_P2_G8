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
    :return: a float.
    """

    # Get the number os seconds passed since epoch
    start_time = time.time()

    return start_time


def toc(start_time):
    """
    Function used to return the elapsed time since function tic() was used. tic() and toc() works together.
    :param start_time: number of seconds passed since epoch given by tic() function. Datatype: float
    :return: a float.
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
    :return: all statistics to be print after
    """
    # Initialize list of inputs
    input_list = []

    # Counter for the number of inputs
    number_inputs = 0
    number_of_hits = 0

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
                    input_tuple = Input(requested=chr(low_case), received=pressed_key, duration=type_elapsed_time)
                    input_list.append(input_tuple)

                    # Check the pressed key with the random low case letter
                    if pressed_key == chr(low_case):
                        print('You typed letter ' + Fore.GREEN + pressed_key + Fore.RESET)
                        number_of_hits += 1
                        #idx_hit.append(number_inputs)
                        #type_hit_average_duration.append(type_elapsed_time)
                    else:
                        print('You typed letter ' + Fore.RED + pressed_key + Fore.RESET)
                        #type_miss_average_duration.append(type_elapsed_time)

                    number_inputs += 1

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
                print(Fore.RED+'----ATENTION----'+Fore.RESET)
                print('\nYou pressed the space bar, test aborted.')
                exit(0)

            # Create tuple with requested and received key with its durations and append to a list for the dict later on.
            input_tuple = Input(requested=chr(low_case), received=pressed_key, duration=type_elapsed_time)
            input_list.append(input_tuple)

            # Check the pressed key with the random low case letter
            if pressed_key == chr(low_case):
                print('You typed letter ' + Fore.GREEN + pressed_key + Fore.RESET)
                number_of_hits += 1
                #type_hit_average_duration.append(type_elapsed_time)
            else:
                print('You typed letter ' + Fore.RED + pressed_key + Fore.RESET)
                #type_miss_average_duration.append(type_elapsed_time)

            number_inputs += 1

    type_average_durations = [type_duration.duration for type_duration in input_list]
    type_hit_average_duration=[type_duration.duration for type_duration in input_list if \
                               type_duration.requested == type_duration.received]
    type_miss_average_duration= [type_duration.duration for type_duration in input_list if \
                                 type_duration.requested != type_duration.received]

    return input_list, number_inputs, number_of_hits, type_average_durations, type_hit_average_duration, \
           type_miss_average_duration

def pprint_color(obj):
    print(highlight(pformat(obj), PythonLexer(), Terminal256Formatter()))
