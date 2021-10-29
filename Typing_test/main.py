#!/usr/bin/python3

# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
import argparse
from collections import namedtuple
from time import time, ctime
from colorama import Fore, Back, Style
from numpy.random import randint
from my_classes import *
from my_functions import *
import readchar
import json


# --------------------------------------------------
# Script of a typing test - Assignment 1. Examples of similar softwares here: https://www.typingtest.com/
#                                                                             https://www.youtube.com/watch?v=6tRTOd5vPH8
#
# Contributors:
#   - Lucas Rodrigues Dal'Col
#   - Vinícius Campos Batista
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

    # Ask to press any key to start.
    if args['use_time_mode']:
        print('You are in time mode and you have ' + Fore.RED + str(args['max_value']) +
              Fore.RESET + ' seconds to complete the test.')
    else:
        print('You are in maximum number of inputs mode and you have ' + Fore.RED + str(args['max_value']) +
              Fore.RESET + ' inputs available to complete the test.')
    print("Press any key to start the the test.")
    readchar.readkey()

    # Initialize parameters dict
    parameters = {}
    list= []
    # Counter for the number of inputs
    number_inputs = 0
    number_of_hits = 0


    # While cycle for each time mode
    start_time = time()
    parameters['test_start'] = ctime()

    while (number_inputs < args['max_value'] and args['use_time_mode'] is False) \
            or (args['use_time_mode'] is True and time() - start_time < args['max_value']):

        # Generate random low case letter
        low_case = randint(97, 122)
        print('Type letter ' + Fore.BLUE + chr(low_case) + Fore.RESET)

        type_time_init=time() #tempo de resposta
        # Get pressed key from keyboard
        pressed_key = readchar.readkey()
        type_time_end=time() #fim do tempo de reposta
        # Analyse pressed key to see if it's a space, to stop the code.
        if pressed_key == str(' '):
            break

        # Check the pressed key with the random low case letter
        if pressed_key == chr(low_case):
            print('You typed letter ' + Fore.GREEN + pressed_key + Fore.RESET)
            number_of_hits += 1
        else:
            print('You typed letter ' + Fore.RED + pressed_key + Fore.RESET)

        number_inputs += 1
        key= (chr(low_case),pressed_key,type_time_end - type_time_init)
        list.append(key)
    end_time= time()
    print('The test is over. See you next time!')

    parameters['test_end'] = ctime()
    parameters['number_of_types'] = number_inputs
    parameters['number_of_hits'] = number_of_hits
    parameters['number_of_misses'] = number_inputs - number_of_hits
    parameters['accuracy'] = number_of_hits/number_inputs
    parameters['test_duration'] = end_time-start_time
    parameters['types'] = list
    print(json.dumps(parameters, indent=4))


if __name__ == "__main__":
    main()
