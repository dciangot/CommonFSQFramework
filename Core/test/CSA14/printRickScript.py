#!/usr/bin/env python

####################################################
#Use this script to parse comma-delimited files (.csv) created from Rick's excel files.  (Just "save as" CSV)
#
#
####################################################

from __future__ import print_function
import csv

TGraphName = "RickCurve"

xVals=[]
yVals=[]
with open('Rick_datapoints.csv','r') as f:


    dataPoints=csv.reader(f)
    dataPoints.next()
    dataPoints.next()
    dataPoints.next()


    i = 0
    for x,y in dataPoints:
        xVals.append(x)
        yVals.append(y) 
	print(TGraphName, "->SetPoint(", i, ",", x, ",", y, ");", sep='')
	i = i+1
#print(names)
# ('Mark', 'Matt', 'John', 'Jason', 'Matt', 'Frank', 'Frank', 'Frank', 'Frank')
#print(ages)
# ('32', '29', '67', '45', '12', '11', '34', '65', '78')


