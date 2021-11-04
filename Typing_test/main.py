#!/usr/bin/python3

# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
import argparse
import os
import sys
from collections import namedtuple
from pprint import pprint
from prettyprinter import cpprint
from time import time, ctime
from colorama import Fore, Back, Style
from numpy.random import randint
from my_classes import *
from my_functions import *
from my_functions import Input
import readchar
from statistics import mean
from prettyprinter import set_default_style
from prettyprinter import install_extras
from termcolor import colored, cprint
install_extras(['python'])
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

    # Print the description and the contributors of the typing test.
    print("\nWelcome to our Typing Test. \n\nContributors: \n- Lucas Rodrigues Dal'Col \n- Vinícius Campos de Oliveira "
          "Batista \n- José Pedro Moura Costa Pinto \n- Rodrigo Dinis Martins Ferreira \n\nPSR, University of Aveiro, "
          "November 2021.\n")

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

    # Initialize parameters dict and start date of the test and put in the dict
    parameters = {'test_start': ctime()}

    # Call typing test function for each time mode
    if args['use_time_mode']:
        inputs = typing_test(use_time_mode=True, max_value=args['max_value'])
    else:
        inputs = typing_test(use_time_mode=False, max_value=args['max_value'])

    test_elapsed_time = toc(start_time)
    print('\nThe test is over. Here it is your statistics: \n')

    # Create lists for all type durations
    type_average_durations = [input_namedtuple.duration for input_namedtuple in inputs]
    type_hit_average_durations = [input_namedtuple.duration for input_namedtuple in inputs
                                  if input_namedtuple.requested == input_namedtuple.received]
    type_miss_average_durations = [input_namedtuple.duration for input_namedtuple in inputs
                                   if input_namedtuple.requested != input_namedtuple.received]

    # Add more dictionary keys with the other parameters requested.
    parameters['test_end'] = ctime()
    parameters['number_of_types'] = len(type_average_durations)
    parameters['number_of_hits'] = len(type_hit_average_durations)
    parameters['number_of_misses'] = len(type_miss_average_durations)
    if bool(inputs):
        parameters['accuracy'] = (round(len(type_hit_average_durations) / len(type_average_durations), 2))
    else:
        parameters['accuracy'] = None
    parameters['test_duration'] = round(test_elapsed_time, 2)
    parameters['inputs'] = inputs
    if bool(inputs):
        parameters['type_average_duration'] = round(mean(type_average_durations), 2)
    else:
        parameters['type_average_duration'] = None
    if bool(type_hit_average_durations):
        parameters['type_hit_average_duration'] = round(mean(type_hit_average_durations), 2)
    else:
        parameters['type_hit_average_duration'] = None
    if bool(type_miss_average_durations):
        parameters['type_miss_average_duration'] = round(mean(type_miss_average_durations), 2)
    else:
        parameters['type_miss_average_duration'] = None

    # Pretty print of the dict with colors
    pprint_color(parameters)

    # Print messages to motivate the user according to his accuracy
    if bool(inputs):
        if parameters['accuracy'] == 1:
            cprint('You hit every single one, you are a genius!'
                   , color='white', on_color='on_green', attrs=['blink'])
        elif parameters['accuracy'] == 0:
            cprint('You missed them all, go home and practice!'
                   , color='white', on_color='on_red', attrs=['blink'])
        elif 0 < parameters['accuracy'] < 0.5:
            cprint('You missed more then 50%. Keep practicing!'
                   , color='white', on_color='on_yellow', attrs=['blink'])
        elif 0.5 <= parameters['accuracy'] < 1:
            cprint('You were good, but can be better.'
                   , color='white', on_color='on_blue', attrs=['blink'])

    # Ask to the user if he wants to try again or not.
    if bool(inputs):
        print('\nI bet this was fun!')
    else:
        print('\nYou should have played!')
    answer = str(input(Back.GREEN + 'Do you want to play again?' + Back.RESET + '(y/n): '))

    if answer == 'y':
        os.execv(sys.argv[0], sys.argv)
    else:
        print('\nGoodbye.\nSee you next time.\n')


if __name__ == "__main__":
    main()
