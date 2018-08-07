#!/bin/bash
# Runs the data collection script for the 2016 general election data
# Author: Liam McCann
# Created: August 6th, 2018

BASE_DIR=../
DATA_DIR=$BASE_DIR/data
INPUT_DIR=$BASE_DIR/input_data

STATES=( 'North_Carolina' 'Rhode_Island' )

for ((i=0;i<${#STATES[@]};++i));
do

    state=${STATES[i]}

    python3 get_2016_election_data.py $INPUT_DIR/usa-2016-presidential-election-by-county.csv $DATA_DIR/$state\_2016_data.csv $state

done