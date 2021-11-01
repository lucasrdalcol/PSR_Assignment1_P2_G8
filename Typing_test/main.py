#!/usr/bin/python3

# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
import argparse
import os
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

    # Print the description of the typing test.
    print("Welcome to our Typing Test. \n\nContributors: \n- Lucas Rodrigues Dal'Col \n- Vinícius Campos de Oliveira "
          "Batista \n- José Pedro Moura Costa Pinto \n- Rodrigo Dinis Martins Ferreira \n\n PSR, University of Aveiro, "
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
        input_list, number_inputs, number_of_hits, type_average_durations, type_hit_average_duration, \
        type_miss_average_duration = typing_test(use_time_mode=True, max_value=args['max_value'])
    else:
        input_list, number_inputs, number_of_hits, type_average_durations, type_hit_average_duration, \
        type_miss_average_duration = typing_test(use_time_mode=False, max_value=args['max_value'])

    test_elapsed_time = toc(start_time)
    print('\nThe test is over. Here it is your statistics: \n')

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
        parameters['type_hit_average_duration'] = None
    if bool(type_miss_average_duration):
        parameters['type_miss_average_duration'] = mean(type_miss_average_duration)
    else:
        parameters['type_miss_average_duration'] = None

    # Pretty print with colors
    # cpprint(parameters, sort_dict_keys=True)
    # pprint(parameters)
    pprint_color(parameters)

    if parameters['accuracy'] == 1:
        cprint('You hit every single one, you are a genius!'
               , color='white', on_color='on_green', attrs=['blink'])
    elif parameters['accuracy'] == 0:
        cprint('You missed them all, go home and practice!'
               , color='white', on_color='on_red', attrs=['blink'])
    elif parameters['accuracy'] > 0 and parameters['accuracy'] <= 0.5:
        cprint('You missed more then 50%. Keep practicing!'
               , color='white', on_color='on_yellow', attrs=['blink'])
    elif parameters['accuracy'] > 0.5 and parameters['accuracy'] < 1:
        cprint('You were good, but can be better.'
               , color='white', on_color='on_blue', attrs=['blink'])

    print('\nI bet this was fun, do you want to play again?')
    answer = str(input(Back.GREEN+'Run again?'+Back.RESET + '(y/n): '))

    if args['use_time_mode'] == False and answer == 'y':
        print("Alright let's go again")
        os.system('clear &&./main.py -mv ' + str(args['max_value']))
    elif args['use_time_mode'] == True and answer == 'y':
        print("Alright let's go again!\n")
        os.system('clear && ./main.py -utm -mv ' + str(args['max_value']))
    else:
        print('Goodbye.\nSee you next time.\n')


if __name__ == "__main__":
    main()

