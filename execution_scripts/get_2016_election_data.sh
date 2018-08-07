#!/bin/bash
# Runs the data collection script for the 2016 general election data
# Author: Liam McCann
# Created: August 6th, 2018

BASE_DIR=../
DATA_DIR=$BASE_DIR/data
INPUT_DIR=$BASE_DIR/input_data

python3 getElectionData.py $INPUT_DIR/usa-2016-presidential-election-by-county.csv $DATA_DIR/north_carolina_2016_data.csv
