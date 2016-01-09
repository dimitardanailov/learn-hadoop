#!/usr/bin/env python

# ---------------------------------------------------------------
# This reducer code will input a line of text and
# output <word, total-count>

import sys

last_key = None 
running_total = 0

# -----------------------------------
# Loop thru file
#  --------------------------------
for input_line in sys.stdin:
  input_line = input_line.strip()

  # --------------------------------
  # Get Next Word  
  this_key, value = input_line.split("\t", 1) # the Hadoop default is tab separates key value

  # the split command returns a list of strings, in this case into 2 variables 
  value = int(value)

  # ---------------------------------
  # Key Check part
  # 
  # if this current key is same
  #     as the last one Consolidate 
  # otherwise Emit 
  # ---------------------------------
  if last_key == this_key:
    running_total += value
  else:
    if last_key:
      print( "{0}\t{1}".format(last_key, running_total) )

    running_total = value
    last_key = this_key

if last_key == this_key:
    print( "{0}\t{1}".format(last_key, running_total))
 


