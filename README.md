# PSR_Assignment1_P2_G8
PSR Typing test: Assignment 1 of subject Programação de Sistemas Robóticos at Universidade de Aveiro.
#Speed Typing Test
This program aims to measure your typing accuracy.

# Table of Contents
- [Usage](#usage)
- [Results](#results)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Hello PSR
# Hello again


# Usage
To launch the program, the user can enter 2 additional input arguments: the Maximum Value and/or the User Time Mode.


There are 2 game modes: by number of typed letters and by time in seconds.
The User Time Mode input argument sets the game mode. If its false (as default) the game mode is set by the number of the typed letters. In other hand, if the user call the utm input argument when launching the game, the game mode is set to the seconds of typing.
The Maximum Value input argument sets the end of the test (in runaway seconds or in typed keys).

For example, if the user run the command 
    
    main.py -utm -mv 15 
    
The game will end after 15 seconds of the moment that began.

After the program is launched, user will be informed about the game configurations, and will be asked to press a key.


When the time limit or attempts are reached, the statistics of the game are presented.


# Results

After the end of the test, the game will show to user his performance, by displaying some indicators values.
The list of the presented results is show in the following the table:

Parameter | Description 
--- | --- 
test_duration | total test duration 
test_start | begin test date 
test_end | ends test date
number_of_types | number of inputs 
number_of_hits | number of correct inputs 
accuracy | inputs accuracy (hits/total) 
type_average_duration | average duration of the user answers 
type_hit_average_duration | average duration of the correct user answers 
type_miss_average_duration | average duration of the wrong user answers 
inputs | list of information of each user answer: letter requested, letter received and ellapsed answer time (duration) 

With this program, we guarantee that you'll improve your typing skills.
