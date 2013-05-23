#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import csv
import json

sortie = open("sortie_temp2", "a")

with open('temp2.csv', 'rb') as f:
	csvfile = csv.reader(f)
	for row in csvfile:
		texte = ''.join(row).replace("°",",").replace("'",",").replace('"', ',').replace("N",",").replace("O","")
		sortie.write(texte+"\n")
