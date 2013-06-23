#!/usr/bin/python
#
# Copyright 2013 M.Bonet.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "M.Bonet"
__copyright__ = "Copyright 2013, M.Bonet"
__credits__ = ["M.Bonet"]
__license__ = "GPL"
__version__ = "0.0.1"

import sys
import random

#-- Settings --
_frames = 10
_pins = 10
_balls = 2
_manual_mode = False

#-- Counting number of pins per Throw --
def count_pins(throws):
    return reduce(lambda x, y: x + y, throws)

#-- Check if the Throw counts as Spare --
def check_spare(throws, pins):
    return throws and pins == count_pins(throws)

#-- Check if the Thorw counts as Strike --
def check_strike(throws, pins):
    return throws and throws[0] == pins 
   
#-- Get additional points deserves because Strike or Spare --
def get_additional_points(previous_throws, throws, pins):
    additional = 0
    #-- Check if there is strike --
    if check_strike(previous_throws, pins):
        #-- If there is strike we take all the balls of the current throw --
        additional = count_pins(throws)
        #-- If the current is strike we add 10 additional --
        if check_strike(throws, pins):
            additional += 10
            
    elif check_spare(previous_throws, pins):
        #-- If there is spare we take the first ball additionally --
        additional = throws[0]
    return additional

#-- Adding the extra points to the current Throw --
def update_score(previous_throws, throws, pins):
    additional = get_additional_points(previous_throws, throws, pins)
    return additional + count_pins(throws)

#-- Handle the input of the pins depending of manual_mod off/on --
def _input_pins(pins):
    if _manual_mode:
        return input("Number of knocked pins (max %s):" % pins)
    else:
        return random.randint(0, pins)

def game(frames=_frames, balls=_balls, pins=_pins):

    history = []
    score = 0

    #-- Regular face of the game --
    for frame in range(frames):
        print "Frame number %s" % (frame + 1)
        left_pins = pins
        
        #-- Number of balls per throw --
        for ball in range(balls):
            knocked_pins = _input_pins(left_pins)
            print "%s. Knocked pins: %s" % (ball+1, knocked_pins)
            
            if ball == 0:
                #-- Adding a new record at the bottom --
                history.append([knocked_pins])
            else:
                #-- Adding at the end of the list --
                history[-1].append(knocked_pins)
                        
            #-- Break if no pins left --
            left_pins -= knocked_pins 
            if not left_pins: break

        #-- Update general score --
        previous_throws = history[-2] if len(history) > 1 else []
        score += update_score(previous_throws, history[-1], pins)
        
        print "Left pins: %s" % left_pins
        print "Current Score: %s\n" % score

    #-- Additional throw  --
    if check_strike(history[-1], pins) or check_spare(history[-1], pins):
        print "Additional throw:"   
        knocked_pins = _input_pins(pins)
        print "Knocked pins: %s" % knocked_pins
        score += knocked_pins

        if check_strike([knocked_pins], pins):
            print "Additional throw 2nd ball:"
            knocked_pins = _input_pins(pins)
            print "Knocked pins: %s" % knocked_pins
            score += knocked_pins

        print "Final score: %s" % score

    return history

if __name__ == "__main__":
    game()
