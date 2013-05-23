#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import csv
import json

f = open( 'sample.csv', 'r' )
reader = csv.DictReader( f, fieldnames = ( "Latitude","Longitude","Titre","Résumé" ) )
out = json.dumps( [ row for row in reader ] )
coord_json = open('coord.json','a')
coord_json.write(out)
