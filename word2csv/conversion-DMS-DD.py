#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


sortie = open("output.csv", "a")

with open('donnees-nantes.csv', 'rb') as f:
	csvfile = csv.reader(f, delimiter=';')
	for row in csvfile:
		line = ','.join(row)
		latitudeDMS = line.split(',')[0].replace("N","")
		longitudeDMS = line.split(',')[1].replace("O","").replace("W","")
		print("LatitudeDMS = "+latitudeDMS+"\n"+"LongitudeDMS = "+longitudeDMS+"\n")
		if (line.startswith(',') or line.find("°") == -1):
			sortie.write(line+"\n")
		else:
			#Get latitude value from XX°YY'ZZZ"
			lat1 = latitudeDMS.replace('"','').split('°')[0] #XX
			lat2 = latitudeDMS.replace('"','').split("'")[0].split("°")[1] #YY
			lat3 = latitudeDMS.replace('"','').split("'")[1] #ZZZ
			#Get longitude value
			long1 = longitudeDMS.replace('"','').split('°')[0]
			long2 = longitudeDMS.replace('"','').split("'")[0].split("°")[1]
			long3 = longitudeDMS.replace('"','').split("'")[1]
			#Convert DMS to DD
			latDD = float(lat1)+float(lat2)/60+float(lat3)/3600
			longDD = float(long1)+float(long2)/60+float(long3)/3600
			sortie.write(str(latDD)+","+"-"+str(longDD)+"\n")
			
