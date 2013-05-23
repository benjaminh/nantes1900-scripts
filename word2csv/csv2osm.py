#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import csv


sortie = open("output", "a")

with open('test_osm.csv', 'rb') as f:
	csvfile = csv.reader(f)
	for row in csvfile:
		if (not ','.join(row).startswith(",")):
			sortie.write(','.join(row)+"\n")
