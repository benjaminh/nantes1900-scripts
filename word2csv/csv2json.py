#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import csv
import json

f = open( 'fiches_modifiees.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ("Titre","Latitude","Longitude") )
out = json.dumps( [ row for row in reader ] )
coord_json = open('coord_new.json','a')
coord_json.write(out)
