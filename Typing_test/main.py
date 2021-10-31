#!/usr/bin/python3

# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
import argparse
from collections import namedtuple
from prettyprinter import cpprint
from time import time, ctime
from colorama import Fore, Back, Style
from numpy.random import randint
from my_classes import *
from my_functions import *
import readchar
from statistics import mean
from prettyprinter import set_default_style

set_default_style('light')

# --------------------------------------------------
# Script of a typing test - Assignment 1. Examples of similar softwares here: https://www.typingtest.com/
#                                                                             https://www.youtube.com/watch?v=6tRTOd5vPH8
#
# Contributors:
#   - Lucas Rodrigues Dal'Col
#   - Vinícius Campos de Oliveira Batista
#   - José Pedro Moura Costa Pinto
#   - Rodrigo Dinis Martins Ferreira
#
# PSR, University of Aveiro, November 2021.
# --------------------------------------------------

# ------------------------
##   DATA STRUCTURES   ##
# ------------------------
Input = namedtuple('Input', ['requested', 'received', 'duration'])


def main():
    # ---------------------------------------------------
    # Initialization
    # ---------------------------------------------------
    # Use argparse to give arguments to the script in terminal.
    ap = argparse.ArgumentParser()
    ap.add_argument('-utm', '--use_time_mode', action='store_true',
                    help='Max number of seconds ' + Fore.RED + 'for time' + Fore.RESET +
                         ' mode or maximum number of inputs ' + Fore.RED + 'for' + Fore.RESET + ' number of inputs mode')
    ap.add_argument('-mv', '--max_value', type=int, required=True,
                    help='Max number of seconds ' + Fore.RED + 'for time' + Fore.RESET +
                         ' mode or maximum number of inputs ' + Fore.RED + 'for' + Fore.RESET + ' number of inputs mode')
    args = vars(ap.parse_args())

    # Print the description of the typing test.
    print('Welcome to our Typing Test. \n\nContributors: \n- Lucas Rodrigues DalCol \n- Vinícius Campos de Oliveira '
          'Batista \n- José Pedro Moura Costa Pinto \n- Rodrigo Dinis Martins Ferreira \n\n PSR, University of Aveiro, '
          'November 2021.\n')

    # See which mode is being used and ask to press any key to start.
    if args['use_time_mode']:
        print('You are in time mode and you have ' + Fore.RED + str(args['max_value']) +
              Fore.RESET + ' seconds to complete the test.')
    else:
        print('You are in maximum number of inputs mode and you have ' + Fore.RED + str(args['max_value']) +
              Fore.RESET + ' inputs available to complete the test.')
    print("\nPress any key to start the the test.\n")
    readchar.readkey()  # Block the code waiting for a key to start
    start_time = tic()  # Start the counter of the test

    # Initialize parameters dict
    parameters = {}

    # Initialize list of inputs and durations averages
    input_list = []
    # idx_hit = []
    type_hit_average_duration = []
    type_miss_average_duration = []

    # Counter for the number of inputs
    number_inputs = 0
    number_of_hits = 0

    parameters['test_start'] = ctime()  # Start date of the test and put in the dict

    # While cycle for each time mode
    while (args['use_time_mode'] is False and number_inputs < args['max_value']) \
            or (args['use_time_mode'] is True and time() - start_time < args['max_value']):

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

        # Create tuple with requested and received key with its durations and append to a list for the dict later on.
        input_tuple = Input(requested=chr(low_case), received=pressed_key, duration=type_elapsed_time)
        input_list.append(input_tuple)

        # Check the pressed key with the random low case letter
        if pressed_key == chr(low_case):
            print('You typed letter ' + Fore.GREEN + pressed_key + Fore.RESET)
            number_of_hits += 1
            # idx_hit.append(number_inputs)
            type_hit_average_duration.append(type_elapsed_time)
        else:
            print('You typed letter ' + Fore.RED + pressed_key + Fore.RESET)
            type_miss_average_duration.append(type_elapsed_time)

        number_inputs += 1

    test_elapsed_time = toc(start_time)
    print('\nThe test is over. Here it is your statistics: \n')

    type_average_durations = [type_duration.duration for type_duration in input_list]
    # type_hit_average_duration = [type_average_duration for idx, type_average_duration in enumerate(type_average_durations)]

    # Add more dictionary keys with the other parameters requested.
    parameters['test_end'] = ctime()
    parameters['number_of_types'] = number_inputs
    parameters['number_of_hits'] = number_of_hits
    parameters['number_of_misses'] = number_inputs - number_of_hits
    parameters['accuracy'] = number_of_hits / number_inputs
    parameters['test_duration'] = test_elapsed_time
    parameters['inputs'] = input_list
    parameters['type_average_duration'] = mean(type_average_durations)
    if bool(type_hit_average_duration):
        parameters['type_hit_average_duration'] = mean(type_hit_average_duration)
    else:
        parameters['type_hit_average_duration'] = 0.0
    if bool(type_miss_average_duration):
        parameters['type_miss_average_duration'] = mean(type_miss_average_duration)
    else:
        parameters['type_miss_average_duration'] = 0.0

    # Pretty print with colors
    cpprint(parameters, sort_dict_keys=True)

    print('\nThank you. See you next time.')


if __name__ == "__main__":
    main()
