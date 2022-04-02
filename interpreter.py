#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                  Description                                            #
# Xlang Interpreter version 0.1. Runs a real X program and provides an Interactive Shell  #
# desinged for learning and debugging (aka. xlsh).                                        #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                                    License                                              #
#  Copyright 2022 X contributors. All rights reserved.                                    #
#                                                                                         #
#  Licensed under the Apache License, Version 2.0 (the "License");                        #
#  you may not use this file except in compliance with the License.                       #
#  You may obtain a copy of the License at                                                #
#                                                                                         #
#      http://www.apache.org/licenses/LICENSE-2.0                                         #
#                                                                                         #
#  Unless required by applicable law or agreed to in writing, software                    #
#  distributed under the License is distributed on an "AS IS" BASIS,                      #
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.               #
#  See the License for the specific language governing permissions and                    #
#  limitations under the License.                                                         #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import os
from colorama import *
init() # fix colorama's bug on Microsoft Windows. This bug does not happen on un*x systems. See colorama readme: https://github.com/tartley/colorama#readme
print(f"{Fore.RED}X{Style.RESET_ALL}lang-{fore.CYAN}C{Style.RESET_ALL} Developer Release")
print("Welcome to xlang. Type 'Help' or 'License' for more info.\nTo get out, type 'Exit'.")
while True:
  request = input(">>> ")
  if request.startswith("Print:"):
    print = request.replace("Print:","",1)
    print(print)
  elif request.startswith("System:"):
    com = request.replace("System:","",1)
    # Anyone that maintains a fork of Xlang-C may enable this echo by removing the sharp sign below.
    #print(f"> {com}")
    os.system(com)
  else:
    print(f"Traceback {Style.DIM}(most recent call last){Style.RESET_ALL}:\n       {request}\nError: undefined Xscript '{request}'")
    print("Try https://github.com/XPL-Lang/Xlang-C/wiki for help.")
