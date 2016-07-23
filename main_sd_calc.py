#!/usr/bin/env/python

#Usage:
#  $ python main_sd_calc.py xColName dataSeriesFilename.csv
#  OR takes input from pipe; example:
#  $ cat dataSeriesFilename.csv | python main_sd_calc.py xColName

from csv_col_extractor import extract
from data_series_mean import calculate as mCalculate
from data_series_sd import calculate as sdCalculate
import sys

xColName = sys.argv[1]

with open(sys.argv[2], 'r') if len(sys.argv) > 2 else sys.stdin as srcTSVFile:
    xData = extract(xColName, srcTSVFile)
    srcTSVFile.close()

m = mCalculate(xData)
sd = sdCalculate(m, xData)

print 'Standard Deviation of the series is,', sd